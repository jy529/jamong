def divide_name(name):
    lastName = name[0]
    firstName = name[1:]

    print('ㅡ' * 12)
    print('성:\t' + lastName)
    print('이름:\t' + firstName)
    print('ㅡ' * 12)
    print(' ' * 12)
name = input('당신의 이름은? ')
divide_name(name)