a2 = int(input("Ты спортсмен и занимаешься ежедневными пробежками. Каков твой результат в первый день? в метрах."))
b = int(input("Какое растояние в метрах, ты бы хотел пробежать, всего?"))
date = 1
print("Ты в первый день пробежал " + str(a2) + " м. Каждый последующий будешь пробегать на 10% больше. И сейчас я опишу план пробежек, по которому ты достигнешь своей цели " + str(b) + " м.")
print("День: " + str(date) + " - " + str(a2))
while (a2 <= b):
    date = date + 1
    a2 = float("%.2f" %(a2+(a2*1.1)))
    print("День: " + str(date) + " - " + str(a2))
print("Итого потребуется " + str(date) + " дн., что бы пробежать " + str(a2) + " м.")

# откровенно говоря я совсем не понял
# как тут сложить формулу таким образом
# что бы с минимальным кодом справно выдавать информацию
# часа 4 просидел
# с 3 дня жесть какая-то начинается
