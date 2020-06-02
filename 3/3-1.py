#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
# сто то в скобках функции, деление
#трай ексев можно с ней или без

def my_f(num, num2):
    global n
num = input("Insert number:")
num2 = input("Insert still another number:")
print("Your numbers: " + str(num) + " and " + str(num2))
try:
    num = int(num)
    num2 = int(num2)
    n = num / num2
except (ValueError, ZeroDivisionError):
    print("it's not number or 0.")

print(int(n))






