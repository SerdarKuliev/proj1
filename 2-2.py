#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

a0=input("Введи данные:")
a1=input("Введи данные:")
a2=input("Введи данные:")
a3=input("Введи данные:")
a4=input("Введи данные:")
a5=input("Введи данные:")
a6=input("Введи данные:")
a7=input("Введи данные:")
a8=input("Введи данные:")
a9=input("Введи данные:")
my_list=[a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]
print("Вот что у нас вышло: "+ str(my_list))
print("Теперь попробуем заменить значения соседних элементов!")
my_list[0], my_list[1] = my_list[1], my_list[0]
my_list[2], my_list[3] = my_list[3], my_list[2]
my_list[4], my_list[5] = my_list[5], my_list[4]
my_list[6], my_list[7] = my_list[7], my_list[6]
my_list[8], my_list[9] = my_list[9], my_list[8]
print("Кажется получилось: "+ str(my_list))






