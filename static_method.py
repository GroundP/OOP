'''
    파이썬 메소드의 종류는 3가지 - 인스턴스 메소드, 클래스 메소드, 정적 메소드
    정적 메소드는 인스턴스 변수나 클래스 변수 중 아무것도 사용하지 않을 메소드라면 정적 메소드로 만든다.
'''
class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        print("총 유저 수는: {}입니다".format(cls.count))

    @staticmethod
    def is_valid_email(email_address): # 정적메소드는 자동으로 전달되는 파라미터가 없다.
        return "@" in email_address

# 정적 메소드는 인스턴스,클래스 두 가지 모두를 통해 사용 가능하다.
print(User.is_valid_email("taehosung"))
print(User.is_valid_email("taehosung@codeit.kr"))

print(user1.is_valid_email("taehosung"))
print(user1.is_valid_email("taehosung@codeit.kr"))