with open("ex2.txt", "w+", encoding='utf-8') as ser:
    ser.writelines([input("ВВЕДИ ФИО:"), "\n", input("ВОЗРАСТ:"), "\n", input("ВЕРОИСПОВЕДАНИЕ:"), "\n"])