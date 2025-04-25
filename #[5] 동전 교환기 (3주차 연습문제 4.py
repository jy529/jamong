#[5] 동전 교환기 (3주차 연습문제 4.7)
#📌 문제:
#3520원을 입력받아 500원, 100원, 50원, 10원으로 교환하는 함수 작성
#✅ 답안 코드:



def exchange(money):
    for coin in [500, 100, 50, 10]:
        count = money // coin
        print(f"{coin}원: {count}개")
        money %= coin

amount = int(input("금액 입력: "))
exchange(amount)