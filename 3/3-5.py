#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
#При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и
#снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается.
#Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
#сумме и после этого завершить программу.

def my_func(**kwargs):
    return kwargs
massive = list(map(int, input("any, but not ~: ").split()))
if list != "~":
    sum = 0
    for i in massive:
        sum += i
    print(sum)
    massive.append(map(int, input("more: ").split()))
    if list != "~":
            sum = sum+i
            for i in massive:
                    sum += i
    print(sum)









OK = input("OK?")


