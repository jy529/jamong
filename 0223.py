
cost = int(input('구매한 금액은? '))
payment = int(input('지불받은 금액은? '))
last_money = payment - cost


def show_change_money(amount):
    n10000 = amount // 10000
    amount %= 10000
    n5000 = amount // 5000
    amount %= 5000
    n1000 = amount // 1000
    amount %= 1000
    n500 = amount // 500
    amount %= 500
    n100 = amount // 100
    amount %= 100

    print('>10000원권: ', n10000,'장')
    print('>5000원권: ', n5000,'장')
    print('>1000원권: ', n1000,'장')
    print('>500원권: ', n500,'장')
    print('>100원권: ', n100,'장')

show_change_money(last_money)