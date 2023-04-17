# Many to many Relationship
## 목차
1. 개요
2. ManyToManyField
3. Article & User

## 학습 목표
* ManyToManyField 필드를 사용하여 다대다 관계를 설정할 수 있다.
* 다대다 관계의 생성, 수정, 삭제 등의 작업을 어떻게 수행하는지를 이해하고 활용할 수 있다.
* 다대다 관계에서 중개 모델(intermediate model)이 필요한 이유와 중개 모델을 어떻게 정의하고 활용하는지에 대해 열거할 수 있다.

# 1. 개요
## M:N 관계 맛보기
* 병원 진료 시스템 모델 관계 만들기(환자 - 의사)
* N:1의 한계
  * 동일한 환자지만 다른 의사에게 예약하기 위해서는 객체를 하나 더 만들어서 예약을 진행해야함
  * 새로운 환자 객체를 생성할 수 밖에 없음
  * 외래 키 컬럼에 '1, 2'형태로 참조하는 것은 Integer 타입이 아니기 때문에 불가능

  => "예약 테이블을 따로 만들자"

## 1-1. 중계 모델
* 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 작성
* 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐
```python
# hospitals/models.py

class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
      return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# 중개 모델 작성
class Reservation():
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

* 데이터베이스 초기화 및 Migraion 진행
* 생성된 중개 테이블 확인
  * `hospitals_reservation`
  
  id | doctor_id | patient_id
  :-:|:-:|:-:
  . | . | .
* shell_plus 써보기
  * 의사1과 환자1 생성 후 예약 만들기
  ```shell
  doctor1 = Doctor.objects.create(name='alice')
  patient1 = Patient.objects.create(name='carol')

  Reservation.objects.create(doctor=doctor1, patient=patient1)
  ```
  * 예약 정보 조회
  ```shell
  # 의사 -> 예약 정보 찾기
  doctor1.reservation_set.all()
  <QuerySet <[Reservation: 1번 의사의 1번 환자>]>

  # 환자 -> 예약 정보 찾기
  patient1.reservation_set.all()
  <QuerySet <[Reservation: 1번 의사의 1번 환자>]>
  ```
  * 의사1에게 새로운 환자 예약이 생성된다면
  ```shell
  patient2 = Patient.object.create(name='dane')

  Reservation.objects.creat(doctor=doctor1, patient=patient2)
  ```
  * 의사1의 예약 정보 조회
  ```shell
  # 의사 -> 환자 목록
  doctor1.reservation_set.all()
  <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 1번 의사의 2번 환자>]>
  ```

## 1-2. Django ManyToManyField
* 환자 모델에 Django ManyToManyField 작성(의사모델에서도 가능)
```python
# hospital/models.py

class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# Reservation Class 주석 처리
```
* 데이터 베이스 초기화 후 Migration 진행
* 생성된 중개 테이블 확인
  * `hospitals_patient_doctors`

  id | patient_id | doctor_id
  :-:|:-:|:-:
  . | . | .
* shell_plus 써보기
  * 의사 1명과 환자 2명 생성
  ```shell
  doctor1 = Doctor.objects.create(name='alice')
  patient1 = Patient.objects.create(name='carol')
  patient2 = Patient.objects.create(name='dane')
  ```
  * 예약 생성 (환자가 의사에게 예약)
  ```shell
  # patient1이 doctor1에게 예약
  patient1.doctors.add(doctor1)

  # patient1 - 자신이 예약한 의사 목록 확인
  patient1.doctors.all()
  <QuerySet [<Doctor: 1번 의사 alice>]>

  # doctor1 - 자신의 예약된 환자 목록 확인
  doctor1.patient_set.all()
  <QuerySet [<Patient: 1번 환자 carol>]>
  ```
  * 예약 생성 (의사가 환자를 예약)
  ```shell
  # doctor1이 patient2을 예약
  doctor1.patient_set.add(patient2)

  # doctor1 - 자신의 예약 환자 목록 확인
  doctor1.patient_set.all()
  <QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 dane>]>

  # patient1, 2 - 자신이 예약한 의사 목록 확인
  patient1.doctors.all()
  <QuerySet [<Doctor: 1번 의사 alice>]>

  patient2.doctors.all()
  <QuerySet [<Doctor: 1번 의사 alice>]>
  ```
  * 예약 현황 중개 테이블 확인
  * 예약 취소하기(삭제)
    * 기존에는 해당하는 Reservation을 찾아서 지워야 했다면, 이제는 .remove() 사용
  ```shell
  # doctor1이 patient1 진료 예약 취소
  doctor1.patient_set.remove(patient)

  # patient2가 doctor1 진료 예약 취소
  patient2.doctors.remove(doctor1)
  ```

## 1-3. 'through' argument
* ManyToManyField를 사용할 때 중개 모델을 직접 작성(추가 데이터 작성 가능)
* 중개 테이블을 수동으로 지정하려는 경우 through 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
* 가장 일반적인 용도
  * "중개테이블에 '추가 데이터'를 사용해 다대다 관계와 연결하려는 경우"
* through 설정 및 Reservation Class 수정
* 이제는 예약 정보에 "증상"과 "예약일"이라는 추가 데이터가 생김
```python
# hospital/models.py

...

class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor, through='Reservation') ##
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation():
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()                                    ##
    reserved_at = models.DateTimeField(auto_now_add=True)           ##

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

* 데이터 베이스 초기화 후 Migration 진행
* shell_plus 써보기
  * 의사 1명과 환자 2명 생성
  ```shell
  doctor1 = Doctor.objects.create(name='alice')
  patient1 = Patient.objects.create(name='carol')
  patient2 = Patient.objects.create(name='dane')
  ```
  * 예약 생성 방법 1
  ```shell
  # 1. Reservation class를 통한 예약 생성

  reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
  reservation1.save()

  doctor1.patient_set.all()
  <QuerySet [<Patient: 1번 환자 carol>]>

  patient1.doctors.all()
  <QuerySet [<Patient: 1번 의사 alice>]>
  ```
  * 예약 생성 방법 2
  ```shell
  # 2. Patient 객체를 통한 예약 생성

  patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})

  doctor1.patient_set.all()
  <QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 dane>]>

  patient2.doctors.all()
  <QuerySet [<Doctor: 1번 의사 alice>]>
  ```
  * 예약 삭제
  ```shell
  doctor1.patient_set.remove(patient1)

  patient2.doctors.remove(doctor1)
  ```
## 1-99. 정리
* M:N 관계로 맺어진 두 테이블에는 변화가 없음
* ManyToManyField는 중개 테이블을 자동으로 생성함
  * (through로 추가 데이터 가능)
* ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
* 대신 필드 작성 위치에 따라 **참조**와 **역참조 방향**을 주의할 것
* N:1은 완전한 종속의 관계였지만 M:N은 의사에게 진찰받는 환자, 환자를 진찰하는 의사의 두 가지 형태로 모두 표현이 가능

# 2. ManyToManyField
