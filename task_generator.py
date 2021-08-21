
import random as rnd

def gen_0():
    mx = 9
    ex = '(a + b) * (c - d)'
    a = rnd.randint(-mx,mx)
    b = rnd.randint(-mx,mx) 
    c = rnd.randint(-mx,mx)
    d = rnd.randint(-mx,mx)    
    return subst(ex,['a','b','c','d'],[a,b,c,d]), str(eval(ex))

def gen_1():
    mx = 9
    r = rnd.randint(0,1)
    sign = '+' if r == 0 else '-'
    ex = f'a * b {sign} c * d'
    a = rnd.randint(-mx,mx)
    b = rnd.randint(-mx,mx)
    c = rnd.randint(-mx,mx)
    d = rnd.randint(-mx,mx)
    return subst(ex,['a','b','c','d'],[a,b,c,d]), str(eval(ex))



def gen_2():
    r = rnd.randint(0,1)
    sign = '+' if r == 0 else '-'
    ex = f'a : b {sign} c : d '    
    a,b,res = getQuotient()
    c,d,res_0 = getQuotient()
    ex_1 = ex.replace(':','/')
    return subst(ex,['a','b','c','d'],[a,b,c,d]), str(int(eval(ex_1)))

def gen_3():
    mx = 9
    mn = 3	
    ex = 'a * b * c'        
    a = rnd.randint(mn,mx) 
    b = rnd.randint(-mx,mx) 
    c = rnd.randint(mn,mx) 
    a,b = changeSignes(a,b)
    return  subst(ex,['a','b','c'],[a,b,c]),  str(eval(ex))


def gen_4():
    ex = 'a : b ' 
    a,b,res = getQuotient()
    c = rnd.randint(1,4)
    d = rnd.randint(1,4)
    if (c < d):
        (c,d) = (d,c)
    a = a * (10 ** c) 
    b = b * (10 ** d)
    if a < b:
        (a,b) = (b,a)
    a,b = changeSignes(a,b)
    ex_1 = ex.replace(':','/')
    return subst(ex,['a','b'],[a,b]), str(int(eval(ex_1)))
	


def gen_5():
    mx = 10
    ex = 'a * b '    
    a = rnd.randint(1,mx) * (10 ** rnd.randint(1,4)) 
    b = rnd.randint(1,mx) * (10 ** rnd.randint(2,3))
    a,b = changeSignes(a,b)
    return subst(ex,['a','b'],[a,b]), str(eval(ex))


def gen_6():
    mn = 500
    mx = 20000
    ex = 'a * b'
    a = rnd.randint(mn,mx)    
    b = rnd.randint(2,9)
    a,b = changeSignes(a,b)
    time = 60000
    return subst(ex,['a','b'],[a,b]), str(eval(ex)), time

def gen_7():
    mn = 900
    mx = 20000
    ex = 'a + b'
    a = rnd.randint(mn,mx)
    b = rnd.randint(mn,mx)
    a,b = changeSignes(a,b)
    time = 60000
    return subst(ex,['a','b'],[a,b]), str(eval(ex)), time

def gen_8():
    ex = 'a : b '
    ex_1 = ex.replace(':','/')
    a,b,res = getQuotient(mx_a = 10000,min_a = 800,min_b = 3,mx_b = 9)
    a,b = changeSignes(a,b)
    time = 80000
    return subst(ex,['a','b'],[a,b]), str(int(eval(ex_1))), time

def gen_9():
    mn = 900
    mx = 20000
    ex = 'b - a'
    a = rnd.randint(mn,mx)
    b = rnd.randint(mn,mx)
    a,b = changeSignes(a,b)
    time = 60000
    return subst(ex,['a','b'],[a,b]), str(eval(ex)), time

def get_tasks(N):
    ex = []
    for k in range(N):
        t = rnd.randint(0,9)
        f = 'gen_' + str(t) + '()'
        r = eval(f)
        ex.append(r)
    return ex

def changeSignes(a,b):
    r = rnd.randint(0,3)
    if r == 1:
        a = -a
    if r == 2:
        b = -b
    if r == 3:
        a = -a
        b = -b
    return a,b

def subst(ex,symb,var):
    for s,v in zip(symb,var):
        sub_v = f'({str(v)})' if v < 0 else str(v)
        ex = ex.replace(s,sub_v)
    return ex

def getQuotient(mx_a = 15,min_a = 2,mx_b = 15,min_b = 1):    
    a = rnd.randint(min_a,mx_a)
    b = rnd.randint(min_b,mx_b)
    c = a * b
    return c,b,a