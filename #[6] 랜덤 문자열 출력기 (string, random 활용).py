#[6] 랜덤 문자열 출력기 (string, random 활용)
# 문제:
#8자리 랜덤 문자열을 생성하시오 (영문자+숫자)

#답안 코드:



import random
import string

letters = string.ascii_letters + string.digits
result = ""

for _ in range(8):
    result += random.choice(letters)

print("랜덤 문자열:", result)