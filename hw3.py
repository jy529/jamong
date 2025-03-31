def get_fixed_price(dc, dcprice):
    originprice = dcprice / (1 - dc / 100)
    return originprice


dc = float(input("할인율은? "))
A_put = float(input("A 상품의 할인 된 가격은? "))
B_put = float(input("B 상품의 할인된 가격은? "))


A_price = get_fixed_price(dc, A_put)
B_price = get_fixed_price(dc, B_put)


print('A 상품의 정가는', A_price)
print('B 상품의 정가는', B_price)
