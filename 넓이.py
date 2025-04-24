def get_circle_area(radius):
    result = 3.14 * radius ** 2
    return result

r = float(input('넓이를 구할 원의 반지름은? '))
area = get_circle_area(r)

print(area)
