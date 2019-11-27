class User:
    count = 0 # 클래스 변수

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
        User.count += 1 # 인스턴스가 생성될 때마다 count가 증가됨

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def login(self, my_email, my_password):
        if ( self.email == my_email and self.pw == my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호 입니다.")


user1 = User("김대위", "captain@codeit.kr", "12345")

# user1.login(user1, "captain@codeit.kr", "12345")  ### 에러!
user1.login("captain@codeit.kr", "12345")


user2 = User("강영훈", "younghoon@codeit.kr", "123456")
user3 = User("이윤수", "yoonsoo@codeit.kr", "abcdefg")
user4 = User("서혜린", "lisa@codeit.kr", "123456")

user1.count = 10 # 이 방식은 인스턴스 변수를 설정하는 작업

print(User.count) #생성된 인스턴스의 개수 출력
print(user1.count)
print(user2.count)
print(user3.count)

User.count = 20

print(User.count)
print(user1.count) # 이미 user1의 count라는 인스턴스 변수는 생성이 되부렀으~
print(user2.count)


