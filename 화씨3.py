def fahrenheit_to_celsius(fahrenheit):
   celsius = 5/9 * (fahrenheit - 32)
   return celsius
def get_real(prompt):
   res = float(input(prompt))
   return res

ftemp = get_real('변환하고자 하는 화씨온도는?')
otemp = fahrenheit_to_celsius(ftemp)
print('화씨', ftemp, '도는 섭씨', otemp)