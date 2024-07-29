# SWM-15th Dngint - AI server

openAI - GPT API와 직접적으로 소통하는 API 서버이며,

추후 활용될 여지가 있는 OCR, Langchain 로직이 설계될 수 있음.

## 아키텍쳐

Spring의 layerd 아키텍쳐를 차용하여 비슷한 흐름을 가진다.

### Controller

jpa의 영속성 컨텍스트의 개념에 해당되는 sqlalchemy의 Session을 주입하는 것과,

엔드포인트 데코레이터를 더욱 복잡하게 붙여야 한다는 문제, 애초에 설계부터 클래스 뷰를 지향하지 않는 점으로 인해

controller의 엔드포인트는 모두 함수로 작성한다.

응답을 받고, 응답해주는 작업만 진행한다. Model 객체는 절대 직접적으로 사용되지 않는다.

DB session을 주입받고, 이를 다시 service class 인스턴스를 생성할 때 주입한다.

### Service

비즈니스 로직을 처리하는 단계.

controller에서 serivce class의 인스턴스로 생성되고 의존성 주입을 통해 사용된다.

인스턴스 생성과 동시에 클래스의 인스턴스 멤버로 session객체를 주입해 repository를 생성한다.

repository class를 생성하여 DB와 통신하거나, 데이터를 조작한다.

dto -> model, model -> dto 변환이 이루어져, controller에서 model 객체를 다루지 않도록 만든다.

### Repository

Sqlalchemy를 통해 DB와 직접적으로 소통한다.

contorller의 엔드포인트 함수에서 주입받은 db를 service class를 생성하면서 파라미터로 주입하고,

다시 주입받은 db객체를 repository class의 인자로 주입하여, service class 인스턴스 변수로 선언한다.

따라서 repository 객체의 인스턴스 변수에는 db session 객체가 선언된다.

repository는 serivce에서 self.'domain'repo로 사용한다.

인스턴스 메서드는 self로 접근 가능한 db session 객체를 활용해 db와 직접적으로 소통한다.

데이터 조회, 수정, 저장, 매우 간단한 수준의 조작 등의 일을 처리한다.

### Model

DB 테이블과 매핑되는 Entity는 model의 경우, Bean 컨테이너를 통해 관리하는 방법을 사용할 수 없으므로,

연관관계 매핑에서 상호참조 문제가 없도록 연관되는 모델을 하나의 파일에 함께 선언한다.

방법을 찾아보자.

### Config

환경변수 관리, DB 커넥션 관리 등, 환경 설정에 관한 정보와 코드들의 집합.

### Util

openAI api 연결, type converter, db exception handler 등, 공용으로 쓰이는 모듈의 집합


## 코드 작성 컨벤션

디렉토리 별 파일들의 상세 내역은 위에서 확인 가능하다.

호출이 잦은 util과 service, repository의 파일 별 최상위 클래스들은 해당 디렉토리의 패키지 생성자 파일(__init__.py)에 선언하여 패키지로 묶는다.

dto와 model은 그 수가 많아지므로, 파일에 직접 접근하여 임포트 하는 방식을 쓴다.