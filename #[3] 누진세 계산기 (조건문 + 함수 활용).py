#[3] 누진세 계산기 (조건문 + 함수 활용)
# 📌 문제:
#연소득을 입력받아 다음 조건에 따라 세금을 계산하시오

#1200 이하: 6%

#4600 이하: 15%

#초과: 24%

#✅ 답안 코드:



def calc_tax(income):
    if income <= 1200:
        return income * 0.06
    elif income <= 4600:
        return 72 + (income - 1200) * 0.15
    else:
        return 582 + (income - 4600) * 0.24

salary = int(input("연 소득 입력: "))
print("세금:", int(calc_tax(salary)), "만원")