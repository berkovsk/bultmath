
import random as rnd

def gen_0():
    mx = 15
    ex = '(a + b) * (c - d)'
    a = rnd.randint(3,mx)
    b = rnd.randint(1,mx) 
    c = rnd.randint(4,mx)
    d = rnd.randint(1,c-1)    
    return subst(ex,['a','b','c','d'],[a,b,c,d]), str(eval(ex))

def gen_1():
    mx = 14
    ex = 'a * b + c * d'
    a = rnd.randint(1,mx)
    b = rnd.randint(1,mx)
    c = rnd.randint(1,mx)
    d = rnd.randint(1,mx)
    return subst(ex,['a','b','c','d'],[a,b,c,d]), str(eval(ex))

def gen_2():
    mx = 10
    ex = 'a * b '    
    a = rnd.randint(1,mx) * (10 ** rnd.randint(1,4)) 
    b = rnd.randint(1,mx) * (10 ** rnd.randint(2,3))
    if rnd.randint(0,1) > 0:
        (a,b) = (b,a)
    return subst(ex,['a','b'],[a,b]), str(eval(ex))

def gen_3():
    ex = 'a : b + c : d '    
    a,b,res = getQuotient()
    c,d,res_0 = getQuotient()
    ex_1 = ex.replace(':','/')
    return subst(ex,['a','b','c','d'],[a,b,c,d]), str(int(eval(ex_1)))

def gen_4():
    ex = 'a : b - c : d '    
    a,b,res = getQuotient()
    c,d,res_1 = getQuotient()
    if res < res_1:
        (a,c) = (c,a)
        (b,d) = (d,b)
    ex_1 = ex.replace(':','/')
    return subst(ex,['a','b','c','d'],[a,b,c,d]), str(int(eval(ex_1)))

def gen_5():
    mx = 12
    ex = 'a * b - c * d'
    a = rnd.randint(1,mx)
    b = rnd.randint(1,mx)
    c = rnd.randint(1,mx)
    d = rnd.randint(1,mx)
    if a * b < c * d:
        (a,c) = (c,a)
        (b,d) = (d,b)
    return subst(ex,['a','b','c','d'],[a,b,c,d]), str(eval(ex))

def gen_6():
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
    ex_1 = ex.replace(':','/')
    return subst(ex,['a','b'],[a,b]), str(int(eval(ex_1)))
	
def gen_7():
    mx = 12
    mn = 3	
    ex = 'a * b * c'    
    a = rnd.randint(mn,mx) 
    b = rnd.randint(mn,mx) 
    c = rnd.randint(mn,mx)    
    return  subst(ex,['a','b','c'],[a,b,c]),  str(eval(ex))

def gen_8():
    mn = 500
    mx = 20000
    ex = 'a * b'
    a = rnd.randint(mn,mx)
    b = rnd.randint(2,9)
    time = 60000
    return subst(ex,['a','b'],[a,b]), str(eval(ex)), time

def gen_9():
    mn = 900
    mx = 20000
    ex = 'a + b'
    a = rnd.randint(mn,mx)
    b = rnd.randint(mn,mx)
    time = 60000
    return subst(ex,['a','b'],[a,b]), str(eval(ex)), time

def gen_10():
    ex = 'a : b '
    ex_1 = ex.replace(':','/')
    a,b,res = getQuotient(mx_a = 10000,min_a = 800,min_b = 3,mx_b = 9)
    time = 80000
    return subst(ex,['a','b'],[a,b]), str(int(eval(ex_1))), time

def gen_11():
    mn = 900
    mx = 20000
    ex = 'b - a'
    a = rnd.randint(mn,mx - 1)
    b = rnd.randint(a + 1,mx)
    time = 60000
    return subst(ex,['a','b'],[a,b]), str(eval(ex)), time

def get_tasks(N):
    ex = []
    for k in range(N):
        t = rnd.randint(0,11)
        f = 'gen_' + str(t) + '()'
        r = eval(f)
        ex.append(r)
    return ex


def subst(ex,symb,var):
    for s,v in zip(symb,var):
        ex = ex.replace(s,str(v))
    return ex

def getQuotient(mx_a = 15,min_a = 2,mx_b = 15,min_b = 1):    
    a = rnd.randint(min_a,mx_a)
    b = rnd.randint(min_b,mx_b)
    c = a * b
    return c,b,a