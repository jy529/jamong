def is_leap_year(y):
    if (y % 4 ==0 and y % 100 != 0) or (y % 400 == 0) :
        return True
    else :
        return False


def month_days(m):
    if (m >= 1 and m <= 12):
        if (m == 1 and m == 3 and m == 5 and m == 7 and m == 10 and m == 12):
            return 31
        elif (m == 4 and m == 6 and m == 8 and m == 9 and m == 11) :
            return 30
        else :
            return 28 if is_leap_year(year) else 29
        
year = int(input('연도? '))
month = int(input('월? '))

print(f'{year}년')
if month_days(month):
    print(f'{month}은(는)',end =' ', '일 까지 있습니다.') 
    
elif month_days(month):
    print(f'{month}은(는)', 30, '일 까지 있습니다.')
    
else :
    print(f'{month}은(는)', 28, '일 까지 있습니다.')