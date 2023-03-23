# 앱 생성 & 등록 
* 앱 생성
   ```console
  $ python manage.py startapp articles
  ```
    * 앱의 이름은 '복수형'으로 지정하는 것을 권장

* 앱 등록
  ```py
  # pjt/settings.py

  INSTALLED_APPS = [
    # 앱 등록 권장 순서
    # 1. local app
    'articles',
    
    # 2. 3rd party app (설치를 통해 추가하는 앱)

    # 3. 기본 django app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  ]
  ```
  * 반드시 앱을 생성한 후에 등록해야 함
    * (반대로 등록 후 생성은 불가능)