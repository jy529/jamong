def input_age():
    n = int(input('나이?'))
    while n <= 0 or n >= 150:
        n = int(input('나이?'))
    if n >= 20:
        print('당신은 성인입니다.')
    else:
        print('당신은 성인이 아닙니다.')

    
input_age()