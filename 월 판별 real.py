def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    else:
        return False
    
def month_days(year, month):
    if (month >= 1 and month <= 12):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
    
        elif month in [4, 6, 9, 11]:
            return 30
    
        else:  
            return 29 if is_leap_year(year) else 28


year = int(input('연도? '))
month = int(input('월? '))
    
    
days = month_days(year, month)
    
    
print(f"{year}년 {month}월은 {days}일까지 있습니다.")

