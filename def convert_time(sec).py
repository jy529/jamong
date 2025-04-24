def convert_time(sec):
    s = sec
    h = s // 3600
    s = s % 3600

    m = s //60
    s = s % 60

    print(sec, '초는', h, '시간', m, '분', s, '초이다.')

def get_integer(prompt):
    res = int(input(prompt))
    return res
sec = get_integer('변환하고자 하는 시간(초)는?')

convert_time(sec)
