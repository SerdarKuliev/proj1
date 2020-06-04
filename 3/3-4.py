#Программа принимает действительное положительное число x и целое отрицательное число y.
#Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
#При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#1 попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
#2 более сложная реализация без оператора **, предусматривающая использование цикла.
#** первое + второе - отсикать не такие. тестировать через  ** или

# ver.1------------------------------------------
def fun1(x,y):
     return int(''.join(str(int(x)**int(y))))
x=input("1.Insert number 1: ")
y=input("1.Insert number 2: ")
print((fun1(x,y)))

# ver.2 ----------------------------------------------------------------------------------------------------
print((lambda a, b: int(a)**int(b))(a=input("2.int A: "), b=input("2.int B: ")))

# ver.3 ------------------------------------------------
def p(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 != 0:
        return a * p(a, n - 1)
    elif n % 2 == 0:
        return p(a * a, n / 2)

a = float(input("3.1:"))
n = int(input("3.2:"))
print(p(a, n))

# ver.4 ------------------------------------------------------------------------------
def v():
    v1 = int(input("4.Укажите 1: "))
    v2 = int(input("4.Укажите 2: "))
    v3 = v1 ** v2
    return v3
v4 = v()
print(v4)

# ver.5 ---------------------------------------------------------------------------
def my_f():
    x=int(input("5.Inumber 1: "))
    y=int(input("5.Inumber 2: "))
    return (pow(x,y))
o = my_f()
print (o)