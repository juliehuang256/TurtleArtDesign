def XD(t,c,s):
    for x in range(15):
        t.forward(s)

def XP(t,c,size):
    t.color(c)
    for x in range(25):
        t.circle(x)
        t.forward(size)
        t.right(1)
