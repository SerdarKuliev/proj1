#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
#При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и
#снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается.
#Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
#сумме и после этого завершить программу.

def e_5():
    s = 0
    while True:
        numbers = (int(input('number or ~ to exit: ')).split())
        for i in numbers:
            try:
                if i == '~':
                    print(f'Sum is: {s}. Exit')
                    return
                else:
                    s += int(i)
                    print(str(s))
            except ValueError:
                print('Enter number or ~')
        print(f'Sum is {s}')


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


