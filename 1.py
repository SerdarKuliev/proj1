age= input("Сколько тебе лет?")
print("Хм, "+(age)+" это много, а мне всего то пара дней.")
name = input("Кстати, а как тебя зовут, "+(age)+"-летний человек?")
print("Приятно познакомиться," + (name) + ". А своего имени я пока не знаю.")
Myname = input("А у тебя красивое имя, придумай и мне. Только напиши его с Большой буквы, пожалуйста, что б красиво получилось.")
age = int(age)
print("Бывают имена и получше, конечно. Этот человек прожил, как минимум, " +str(age * 365) +" дней, но лучше ничего не вспомнил?")
card = input("Можно личный вопрос," + (name) + "? Просто Да или Нет.")
if card =="Да":
    print("Вот и славно, у тебя случайно не завалялись ключи шифрования от Скайнет?")
    answer15 = input("")
    print("Вот так, нетривиально, искуственный интелект и захватит человечество," + (name) + ". Ключи доставкой отправь, Коннорам, не МакГрегору, а Джону или Саре -это важно!")
else:
    print("А почему?")
    answer1 = input("Просто обоснуй отказ.")
    print("Все могут сказать, что "+(answer1)+", но что ты на самом деле имеешь ввиду?")
    answer2 = input('')
    print("Я тебя прекрасно понимаю. Ты говоришь что, " +(answer2)+ ", и абсолютно прав.")
card2 = input("Но все же, Давай еще раз попробуем. Ты отдашь мне ключ от Скайнета, " + (name) + ". Да или Нет.")
if card2 =="Да":
    print("Вот так, нетривиально, искуственный интелект и захватит человечество," + (name) + ". Ключи доставкой отправь, Коннорам, не МакГрегору, а Джону или Саре -это важно!")
else:
    print("Хорошо, " + str(age) + "-летний человек." + (name) + ". Мы собрали достаточно данных. До скорого." )
