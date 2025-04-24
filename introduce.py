def introduce(name, age):
    firstName = name[1:]
    return f'{firstName}은 내년에 {age + 1}학년입니다.'

n = input('이름? ')
a = int(input('학년? '))

rmsg = introduce(n, a)
print(rmsg)