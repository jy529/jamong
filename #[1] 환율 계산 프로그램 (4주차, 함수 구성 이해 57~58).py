#[1] 환율 계산 프로그램 (4주차, 함수 구성 이해 57~58)
#문제:
#1달러 = N원으로 입력받고,

#원화를 달러로, 달러를 원화로 바꿔주는 함수들을 작성하시오.

#답안 코드:

exchange_rate = 0

def set_rate(won):
    global exchange_rate
    exchange_rate = won

def get_rate():
    return exchange_rate

def to_dollar(won):
    return won / exchange_rate

def to_won(dollar):
    return dollar * exchange_rate

def main():
    set_rate(int(input("오늘의 환율? ")))
    print("2020 원 =", to_dollar(2020), "달러")
    print("2 달러 =", to_won(2), "원")

main()