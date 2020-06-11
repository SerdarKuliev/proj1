
#Var1-------------------------------------------------------------
with open("ex1.txt", "w+", encoding='utf-8') as ser:
    ser.writelines([input("ВВЕДИ ФИО:"), "\n", input("ВОЗРАСТ:"), "\n", input("ВЕРОИСПОВЕДАНИЕ:"), "\n"])

#Var2------------------------------------------------------------- Но он не работает почему-то
with open("ex1.txt", "w+", encoding='utf-8') as ser:
    def serd():
        try:
            ser.writelines([input("ВВЕДИ ФИО:"),"\n", input("ВОЗРАСТ:"),"\n", input("ВЕРОИСПОВЕДАНИЕ:"),"\n"])
            return
        except ValueError:
            return "the end"
print(serd)