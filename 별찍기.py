# 1
for i in range(5):
	print("*")


# 2
print("*" * 5)


# 3
for i in range(5):
	print("*" * 5)


# 4
for i in range(5):
	print((i+1) * "*")


# 5
for i in range(5,0,-1):
    print("*"*i)


#6
for i in range(5):
    for j in range(4-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()


# 7
for i in range(5):
    for j in range(i):
        print(" ",end="")
    for j in range(5-i):
        print("*",end="")
    print()


# 8
for i in range(5):
    for j in range(4-i):
        print(" ",end="")
    for j in range(2*(i+1)-1):
        print("*",end="")
    print()


# 9
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()


# 10
for i in range(1,10):
    if i <= 5:
        for j in range(5-i):
            print(" ",end="")
        for j in range(2*i-1):
            print("*",end="")
        print()
    else:
        for j in range(i-5):
            print(" ",end="")
        for j in range((10-i)*2-1):
            print("*",end="")
        print()
