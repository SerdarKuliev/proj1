генератор, тест исходный список

my_list = [1, 2, 3, 4, 5, 6]
new_list = [i +10 for i in my_list if i % 2 == 0]
print(new_list)

my_list = [1, 2, 3, 4, 5, 6]
my_sec_list =[11, 22, 33, 44, 55]
new_list = [i + j for i in my_list if i % 2 == 0 for j in my_sec_list]
print(new_list)


new_list = {el: el*3 for el in range(10,20)}
print(new_list)

list(range(10,21))

my_tup = (1, 2, 3, 4, 5, 6)
new_obj = [i + 3 for i in my_tup if i % 2 == 0 for j in my_sec_list]
print(len(new_obj))

print(next(new_obj))
print(list(new_obj))