n1 = int(input('피젯수를 정수로 입력하시오: '))
n2 = int(input('젯수를 정수로 입력하시오: '))

def show_division(dividend, divisior) :
    quotient = dividend // divisior
    remainder = dividend % divisior
    print('몫= ', quotient)
    print('나머지=', remainder)
    pass

print(show_division(n1,n2))