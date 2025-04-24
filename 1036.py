def get_radius(prompt):
    r= int(input(prompt))
    return r

radius = get_radius('넓이를 구하고자 하는 원의 반지름? ')

def get_circle_area():
    s = radius**2*3.14
    return s

area = get_circle_area()

print('반지름이', radius, '인 원의 넓이 =', '3.14 X ', radius, 'x', radius, '=', area)