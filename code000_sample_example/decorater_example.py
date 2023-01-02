# 데코레이터 함수 정의
def deco_func(input_func): # 원래 함수를 매개변수로 받음
    def wrapper():
        print("준비")
        input_func() # 원래 함수 실행
        print("완료")
    return wrapper # 데코레이터가 붙은 함수를 리턴

@deco_func
def game():
    print("게임 접속")
    for num in range(0, 10):
        print(str(num)+"시간이 지났습니다")
    print("게임이 종료되었습니다")
    
game()