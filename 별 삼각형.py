n = int(input("높이? "))

for i in range(1, n+1):
    result = "" 
    for j in range(1, i+1):
        result += "*" 
    print(" " * (n - i) + result) 
