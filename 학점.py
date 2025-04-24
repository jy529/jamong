def get_grade(s) :
    if s >= 90 :
        return 'A'
    elif s >= 80 :
        return 'B'
    elif s >= 70 :
        return 'C'
    elif s >= 60 :
        return 'D'
    else :
        return 'B'
    
score = int(input('점수는? '))

grade = get_grade(score)

print(f'{score}점이므로 학점은 {grade}입니다.')