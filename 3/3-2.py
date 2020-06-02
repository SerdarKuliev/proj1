#именнованные аргументы




def my_f():
    global n #nonlocal
    r1 = 56
    r2 = 57
    r3 = 58
    n =(r1*r2)/r3
    total = n**5
    return total
print(my_f())
print(n)