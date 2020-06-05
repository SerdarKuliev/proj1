def gen():
    for i in(10, 20, 30 ,40):
        yield i

for el in gen():
    print(el)


умножение редьюс