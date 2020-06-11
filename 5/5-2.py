ser = open("ex2.txt", "w+", encoding='utf-8')
ser.writelines([input("ВВЕДИ ФИО:"), "\n", input("ВОЗРАСТ:"), "\n", input("ВЕРОИСПОВЕДАНИЕ:"), "\n"])
con = 0
for line in ser:
    con += 1
print(con)
ser.close()