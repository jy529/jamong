def get_fixed_price(discount_rate, discounted_price):
    original_price = discounted_price / (1 - discount_rate / 100)
    return original_price

# 사용자 입력 받기
discount_rate = float(input("할인율은? "))
price_a = float(input("A 상품의 할인 된 가격은? "))
price_b = float(input("B 상품의 할인된 가격은? "))

# 정가 계산
a_original = get_fixed_price(discount_rate, price_a)
b_original = get_fixed_price(discount_rate, price_b)

# 결과 출력
print(f"A 상품의 정가는 {a_original:.2f}")
print(f"B 상품의 정가는 {b_original:.2f}")
