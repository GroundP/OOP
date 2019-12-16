def add_print_to(original): # 함수를 넘겨줌, add_print_to함수는 데코레이션 함수
    def wrapper():
        print("함수시작") # 데코레이션 (넘겨받은 함수의 앞뒤 등등을 꾸며준다)
        original()
        print("함수 끝")

    return wrapper  # 정의된 함수를 반환

@add_print_to  # 골뱅이 요부분을 붙이면, 앞으로 print_hello()만 호출해도 데코레이터 함수가 같이 불린다
def print_hello():
    print("안녕하세요!")

# 함수위에 골뱅이가 보이면 아! 데코레이터구나! 라고 생각하자

print_hello()