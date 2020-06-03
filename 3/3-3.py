#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
# главное не идти на поводу у задачи 2-3 строчки

def my_f(w1, w2, w3):
    global n
    n =(w1-w2)+w3
    total = n**2
    return total
max(str(my_f(5,9,2)))
print(my_f(5,9,2))



w1 = 5 #input("Insert number: ")
w2 = 9 #input("Insert number: ")
w3 = 2 #input("Insert number: ")

