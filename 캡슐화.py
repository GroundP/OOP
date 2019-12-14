"""
데코레이터를 통한 캡슐화
@property
@xxx.setter
위의 모습으로 getter, setter를 데코레이터 형태로 정의한다.
"""

class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        self.name = name
        self._age = age
        self._resident_id = resident_id

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self._resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self._age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는" + str(self._age) + "살입니다."

    @property
    def age(self):
        """Property 데코레이터로 getter함수 정의"""
        print("나이를 리턴합니다")
        return self._age

    @age.setter
    def age(self, value):
        """Property 데코레이터로 setter함수 정의"""
        print("나이를 {}으로 설정합니다.".format(value))
        if value < 0:
            print("나이를 음수로 설정할 수 없습니다. 0으로 초기화 하겠습니다.")
            self._age = 0
        else:
            self._age = value


young = Citizen("박지상", 30, "1222712")
print(young.age) #인스턴스 변수는 _age이지만 데코레이터 getter로 정의된 age메소드를 통해 _age반환
young.age = 21  #인스턴스 변수는 _age이지만 데코레이터 setter로 정의된 age메소드를 통해 _age 설정
print(young.age)