def is_even_number(n) :
    if n % 2 == 0 :
        return True
    else :
        return False
    
num = int(input('정수를 입력하세요: '))

print(f'{num}은(는)', end=' ')
if is_even_number(num) :
    print('짝수', end=' ')
else :
    print('홀수', end =' ')
print('입니다.')