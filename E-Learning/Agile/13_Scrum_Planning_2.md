# 스크럼 계획 수립(II)
## 학습 내용
1. 유저 스토리(User Story)
2. 페르소나(Persona)
## 학습 목표
* 유저 스토리의 가치와 작성 방법을 이해합니다.
* 페르소나의 목적을 이해합니다.

# 1. 유저 스토리(User Story)
* 유저 스토리는 유저입장에서 정의한 기능에 대한 간단한 설명
* 유저 스토리는 한 두 문장으로 구성됨
  * 사용자의 언어(사용자가 잘 이해할 수 있는 포현)로 작성하며, 역할과 목표 정도만 표현함
* 유저 스토리는 작업량 산정(Estimation)의 용도로 사용됨
* 유저 스토리(User Story)의 핵심 구성 요소
  * **<u>역할(Role) : 누가 원하는가?</u>**
  * **<u>목표(Goal) : 무엇을 원하는가?</u>**
  * **<u>이유(Reason) : 왜 원하는가?</u>**
* 스토리 카드
  * 대화의 증거(Tokens for conversations)
  * 공식 문서가 아님(NOT official documents)
* 유저 스토리의 역할
  * 토론(Discussion)
  * 일정 관리(Scheduling)
  * 산정(estimation)
  * 기능 테스트(Functional testing)
  * 완료 여부 판단(Completion)
* 유저 스토리 관리
  * 유저 스토리는 카드 또는 포스트잇에 쓰여짐
  * **유저 스토리는 하나의 스프린트(Iteration, Timebox, Iteration) 안에서 구현하고 테스트함**
  * 유저 스토리는 제품 책임자 또는 고객이 작성. 고객이 작성하면 좀 더 쉽게 쓸 수 있음
  * 유저 스토리를 만들기 위하여 자주 고객을 만날 수 있어야 함
  * **기능(Feature) 관련 유저 스토리는 인수 테스트(Acceptance Test)를 포함함**
* **애자일 WBS**(Work Breakdown Structure)
  * 테마(Theme) > 에픽(Epic) > 기능(Feature) > 유저 스토리(User Story)
  * 에픽 : 유저 스토리의 상위 개념  \
  유저 스토리와 관계된 기능 또는 모듈의 집합
  * 테마 : 에픽의 상위 개념. 서브 시스템(Sub System), 제품 구성 요소, 서비스 등
* 제품 책임자(Product Owner)
  * 제품 책임자는 전반적인 제품 리더십을 발휘하여 의사결정을 함
  * 제품 전략(Product Strategy), 제품 로드맵(Product Roadmap), 제품 백로그(Product Backlog), 이해관계자 관리(Stakeholder Management)
  * **제품 백로그**로부터 해당 스프린트에 할당할 **스프린트 백로그**를 도출한 후에, 팀은 스프린트 내에서 이를 구현할 것을 결정함
  * 제품 책임자는 **우선순위(Priority)**에 따라 다음 스프린트에 작업할 백로그를 선정함
* 기능 책임자(Feature Owner)
  * 개발팀의 팀원은 기능 책임자 역할을 함
  * 기능 책임자(Feature Owner)는 각 기능을 정의하고, 개발하고, 스스로 검증하고, 관리함
* 프로젝트 초기에는 제품 책임자가 기능 정의를 주도함
* 스프린트를 시작하면, 개발팀의 각 기능 책임자가 기능 정의를 주도함
* 제품 백로그의 구성 요소인 유저 스토리에는 **역할(Role), 목표(Goal), 이유(Reason)**를 기술
  * 역할
  * 목표
  * 이유
  * 인수 기준(Acceptance Criteria)
  * 중요도(Importance) = 우선순위(Priorty)
  * 작업량(Estimate)
  * 종류(Type)
* 유저 스토리를 효과적으로 수집하려면
  * 고객이 협력적(Collaborative)이어야 함
  * 고객사 담당자가 대표성(Representative)이 있어야 함
  * 고객사가 유저 스토리를 공식적으로 제공(Authorized)해야 함
  * 프로젝트 팀 뿐만 아니라 고객도 열정적으로(Committed) 참여해야 함
  * 고객도 제품에 대한 이해(Knowledgeable)를 가지고 있어야 함
* 좋은 유저 스토리가 되기 위함 6가지 조건
  * 독립적임
  * 협상 가능함
  * 사용자와 고객에게 가치가 있음
  * 공수의 추정이 가능함
  * 작음
  * 테스트가 가능해야 함
* Adaptive Software Development(ASD)
  * 적응형 소프트웨어 개발 방법론
  * Feature Card
* 애자일 방법론의 제품 정의(Agile Product Definition)
  | 애자일 방법론 | 제품의 정의 방법 | 학자 |
  |:-:|:-:|:-:|
  |**스크럼**|유저 스토리|켄 슈와버, 제프 서덜랜드|
  |**익스트림 프로그래밍(XP)**|유저 스토리|켄트 벡, 에릭 감마|
  |칸반(Kanban)|칸반 카드(Kanban Card)|다이이치 오노(Taiichi Ohno)|
  |크리스털(Crystal)|유스 케이스(Use Case)|앨리스테어 코번|
  |기능 주도 개발 방법론<br>(Feature Driven Development, FDD)|피처 셋(Feature Sets)|피터 코드, 제프 드루카|
  |적응형 소프트웨어 개발 방법론<br>(Adaptive Software Development, ASD)|피처 카드(Feature Cards)|짐 하 이스미스|
  * 모든 애자일 방법론들은 제품을 정의하는 방법을 제시함
    * 고객이 제품의 법위를 결정하는데 적극적으로 참여함
    * 제품 범위는 체계적인 문서보다는 대화 형식으로 제시함
    * 간단하게 속기로 기능을 설명함

# 2. 페르소나(Persona)
* 가상의 사용자(User) 프로필
* 유사한 특성이나 니즈를 가진 사용자 그룹의 표본을 보여주기 위하여 페르소나에는 가상의 개인 정보와 사진이 포함됨
* 스크럼 팀은 사용자와 이해관계자를 보다 잘 이해하기 위하여 유저 스토리와 작업을 정의할 때 페르소나를 검토함
* 페르소나에 각 사용자의 역할에 맞는 사진을 추가하고 사용자에게 동기를 부여하는 요소들을 기술함
* 이렇게 함으로써 개발 대상(What to develop)과 개발 방식(How to develop)을 보다 구체화할 수 있음
* 페르소나를 에픽과 유저 스토리로 발전시킴
  * 스크럼 보드에 유저 스토리를 페로소나 별로 구성함
* 페르소나를 정의하는 방법
  * 설문과 서베이, 박람회에서 인터뷰하기, 브레인스토밍 등