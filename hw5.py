def read_single_digit(N): 
    if N == 0:
        return "영"
    elif N == 1:
        return "일"
    elif N == 2:
        return "이"
    elif N == 3:
        return "삼"
    elif N == 4:
        return "사"
    elif N == 5:
        return "오"
    elif N == 6:
        return "육"
    elif N == 7:
        return "칠"
    elif N == 8:
        return "팔"
    elif N == 9:
        return "구"
    else:
        return "잘못된 입력"

num = input('세 자리 정수 입력: ')

first = int(num[0])  
second = int(num[1])  
third = int(num[2])   
print(read_single_digit(first), read_single_digit(second), read_single_digit(third))
