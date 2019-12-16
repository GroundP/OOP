'''
    인스턴스를 생성할 때 필요한 정보들이 항상 우리가 원하는 형태로 존재할까요? 우리는 다양한 형태의 정보에서 필요한 부분을 뽑아내서 인스턴스를 생성할 수 있어야 합니다.
    예를 들어 유저 인스턴스 생성에 필요한 정보가 문자열일 수도 있고 리스트일 수도 있습니다.
'''

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_param): # 문자열로 인스턴스 만들기
        parameter_list = string_param.split(",")  # split 메소드를 사용해서 쉼표(,)를 기준으로 문자열을 리스트로 분리한다

        # 각 변수에 분리된 문자열 각각 저장
        name = parameter_list[0]
        email = parameter_list[1]
        password = parameter_list[2]

        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_param): # 리스트로 인스턴스 만들기
        name = list_param[0]
        email = list_param[1]
        password = list_param[2]

        return cls(name, email, password)


# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)