from itertools import count, cycle

print('Генератор цифр, что б выйти жми "~"')
for i in count (int(input('inter number: '))):
    print(1, end='')
    quit = input()
    if quit == '~':
        break

print('Генератор цифр, что б выйти жми "+"').split()
list = input('inter number: ')
iter=cycle(list)
quit = None

while quit !=0:
    print(next(iter), end='')
    quit=input()
