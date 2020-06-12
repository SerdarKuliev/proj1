with open ("text_6.txt", "r") as text6:



        s_sum = []
        less = []
        line = ser.read().split('\n')
        for i in line:
            i = i.split()
            if float(i[1]) < 20000:
                less.append(i[0])
            s_sum.append(i[1])

    print(f" Менее 20 000 {less} Средняя {sum(map(float, s_sum)) / len(s_sum)}!")

