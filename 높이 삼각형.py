n = int(input('높이를 입력하세요: '))

for i in range(1, n+1):
    result = ''
    for j in range(1 , i+1):
        result += str(j)
    print(result)