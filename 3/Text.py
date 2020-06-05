
lambda p_1, p_2: p_1+p_2
 print()


 осдедняя условием
работа с символам определенного типа
кв срк len(
    ORD!!!

ord("a")


chr 90=z

abs()
round()

ord("a")
97
ord("A")
65
abs(-90)
90
round(456.789)
457
round(987465464984.7657657657, 5)
987465464984.7657
divmod(8,4)
(2, 0)
pow(2,3)
8
max([11,22,5, -6,2,66,6.7])
66
min([11,22,5, -6,2,66,6.7])
-6

range(8)

list(range(8))
[0, 1, 2, 3, 4, 5, 6, 7]

list(range(5, 8, 2))

for i in range(18)
    print(i/2)

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




try:
    num = int(num)
    num2 = int(num2)
    n = int(num / num2)
    print((str(num)) + ":" + (str(num2)) + "=" + (str(n)))
except (ValueError, ZeroDivisionError):
    print("ERROR, it's 0 or not number.")
OK = input("OK?")


def my_fi():
    name_1 = input("Insert your name:")
    surname = input("Insert your surname:")
    year = input("Insert your year of a birth:")
    town = input("Insert your city:")
    mail = input("Insert your email:")
    phone = input("Insert your phone number:")
print(my_fi(name, surname, year, town, mail, phone))


def my_fi(**kwargs):
    f_1 = input("Insert your name:")
    f_2 = input("Insert your surname:")
    f_3 = input("Insert your year of a birth:")
    f_4 = input("Insert your city:")
    f_5 = input("Insert your email:")
    f_6 = input("Insert your phone number:")
    print(my_fi(f_1, f_2, f_3, f_4, f_5, f_6))

print(my_fi(f_1, f_2, f_3, f_4, f_5, f_6))

OK = input("OK?")

def my_f(f_1=f1, f_2=f2, f_3=f3,f_4=f4, f_5=f5, f_6=f6):
    def my_f(**kwargs):
        return kwargs

    print(my_f(el_1=12, el_2=22, el_3=(1, 2)))
    print(f"Hello")


print(my_f())


def my_f(s1, s2):
    my_sum = s1 + s2
    my_f(12, 22)
    return f"sum:{my_sum})???


print(my_f())


def my_f(**kwargs):
    return kwargs


print(my_f(el_1=12, el_2=22, el_3=(1, 2)))
print(f"Hello")
сумма
чисел
вводит
до
сих
пор
пока
не
введет
спец
символ
Q
gjckt
ckj;
tybz
print(my_f())


def my_f():
    global n
    r1 = 56
    r2 = 57
    r3 = 58
    n = (r1 * r2) + 100 * r3
    total = n ** 5
    return total
    my_sum = s1 + s2
    my_f(12, 22)
    return f"sum:{my_sum})???


print(my_f())

def my_func():
    return
massive = list(map(int, input("any, but not ~: ").split()))
if list != "~":
    sum = 0
    for i in massive:
       sum += i
    print(str(sum))

    if list != "~":
            sum += int(i)
            for i in massive:
                    sum += i
    print(sum)


def my():
    res = 0
    while True:
        numbers = input('Enter numbers or ~ to exit: ').split()
        for i in numbers:
            try:
                if i == '~':
                    print(f'Sum is {res}. Exit')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Enter number or ~')
        print(f'Sum is {res}')







OK = input("OK?")
