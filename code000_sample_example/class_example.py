# 객체지향 프로그래밍
# class : 객체 덩어리 만들기 (설계도)
# instance : class 기반으로 찍어내는 것
# inheritance : 부모 클래스의 자원을 물려받는 것
# 자바의 경우 필드(데이터), 생성자(초기값), 메서드(행위)
# 파이썬은 자바처럼 명확한 규칙이 없으므로, 개발자의 상황에 따라 객체지향 프로그래밍을 할 수 있는 유연성을 갖고 있다 : 자유도 높다 > 규칙이 없다

# 회원정보를 상속받는 포트폴리오 class
# 1. 회원 class의 id, pw, email, name 필드값을 갖는 user1 인스턴스 생성하고, 회원정보를 조회하는 메서드(def)를 만들고 실행하시오
# 2. 포트폴리오 class는 회원 class를 상속받고, 회원의 정보를 조회하는 메서드(def) 실행
# public class className() {}

# class 지정
class account :
    #필드
    id = "abcd"
    pw = "1234"
    email = "a@a"
    name = "김준석"
    #생성자 : 자바와 달리 접근제한자 등 객체지향의 기능들이 default세팅이 되어 있지 않으므로
    #보통 메서드를 활용하여 인스턴스 필드값 생성 및 변경을 진행함
    #ex) 현대프로그래밍은 필드, 생성자, 메서드 또한 분리를 하여 인스턴스를 생성 : go의 메서드를 분리, rust의 필드 분리..
    def __init__(self, input_1, input_2):
        self.id = input_1
        self.pw = input_2

    #메서드 (def : 메서드 선언) (method1 : 메서드 이름) (self : class 자기자신 = this)
    #(self) = 즉, 메서드를 실행할 때 매개변수를 본인을 지정해줘야, 객체을 인식하고 실행
    # : 자바는 온전한 객치지향 프로그래밍 <> 파이썬은 객체지향 프로그래밍을 유사하게 구축
    def method1(self):
        print(self.email)
        print(self.name)
    def setEmail(self):
        print("수정된 이메일 값을 입력하시오")
        self.email = input()

#인스턴스 만들기
#자바 : 타입을 추가, heap메모리 영역을 명확히 표현
#accout accountExample = new account()
accountExample = account()
print(accountExample.id)
print(accountExample.email)
# accountExample.setEmail()
print(accountExample.email)

#자바의 상속과 유사하게 (account) 매개변수를 부모클래스로 받아서 자원을 활용
#파이썬의 상속 = 매개변수를 클래스로 받기
class portfolio(account):
    def __init__(self, input_1, input_2):
        self.id = input_1
        self.pw = input_2
    def infoOutput(self):
        print(self.id)
        print(self.email)

# portfolioExample이라는 변수명은 portfolio class기반의 인스턴스이다
# 인스턴스를 생성할 때 부모클래스 account가 있다
# account의 인스턴스를 먼저 만들고, 매개변수로 portfolio 클래스에 전달한다
# portfolioExample 인스턴스를 생성한다 (부모클래스의 자원은 모두 생성된 상태)
portfolioExample = portfolio("abcd", "1234")
print("-------------")
print(portfolioExample.infoOutput())