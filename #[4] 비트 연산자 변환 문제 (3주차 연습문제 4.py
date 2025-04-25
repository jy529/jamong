#[4] 비트 연산자 변환 문제 (3주차 연습문제 4.6)
#📌 문제:
#n비트를 모두 1로 설정했을 때 10진수와 2진수를 출력하시오.

#✅ 답안 코드:


def set_all_bits(n):
    return (1 << n) - 1

n = int(input("설정할 비트 수는? "))
value = set_all_bits(n)
print(f"{n}비트를 모두 1로 설정한 수는 {value} ({bin(value)})입니다")