'''
    @classmethod 로 표현하는 클래스 메소드는 첫번째 파라미터로 클래스가 자동 전달된다.
    클래스 메소드는 인스턴스 변수를 아예 사용하지 않는 경우에 사용한다.(인스턴스 변수를 알 수 없다)
    인스턴스 변수 사용 -> 인스턴스 메소드
    클래스 변수 사용 -> 클래스 메소드
    둘다 사용 -> 인스턴스 메소드(인스턴스 변수, 클래스 변수 모두 사용 가능)
'''

class User:
    count = 0 # 클래스 변수

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
        User.count += 1 # 인스턴스가 생성될 때마다 count가 증가됨

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        print("총 유저 수는 {} 입니다.".format(cls.count))

user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdefg")
user3 = User("서혜린", "lisa@codeit.kr", "123456")

User.number_of_users()
user1.number_of_users()