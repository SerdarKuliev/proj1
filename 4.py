a =int(input("Т день? в метрах."))
b =int(input("Какое расты бы хотело?"))
date = 1
print("Ты в первый день пробежал " +str(a)+ " м. Каждый последующий будешь пробегать на 10% больше. И сейчас я опишу план пробежек, по которому ты достигнешь своей цели " +str(b)+ " м.")
print("День: " + str(date)+ " - " + str(a))
while(a<=b):
    a = float("%.1f" % (a * 1.1))
    date = date + 1
    print("День: " + str(date) + " - " + str(a))
print("Итого потребуется " + str(date) + " дня, что бы пробежать " + str(a)+ " м.")
