def draw_line_string(name):
    msg1 = 'Hello ' + name
    msg2 = 'welcome to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-',nstr)
    print(msg1,'\n'+msg2)
    rep_char('-',nstr)

def rep_char(s,d):
    print(s*d)

draw_line_string(input("Input his/her name : "))