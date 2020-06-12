try:
    f_obj = open("text.txt", "w")
    for line in f_obj:
        print(line)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f_obj.close()
