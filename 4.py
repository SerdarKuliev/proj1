from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

def add():

    films.append(message.get())
    print(films)
    messagebox.showinfo('Done', 'Добавлен фильм: '+message.get())
    variable = StringVar(root)
    variable.set(films[0])
    w = OptionMenu(root, variable, *films)
    w.place(relx=.3, rely=.3, anchor='c')
def delete():
    messagebox.showinfo('Done', 'Вы добавили фильм '+message.get()+' в список просмотренных')
    print("It is "+message.get())
    f = open('Фильм с follentass.txt', 'w+')
    f.write(''+message.get()+' ')
    try:
        films.remove(message.get())
    except:
        pass
    f.close()
    variable = StringVar(root)
    variable.set(films[0])
    w = OptionMenu(root, variable, *films)
    w.place(relx=.3, rely=.3, anchor='c')

root = Tk()
root.title('Фильмы с follentass')
root.geometry('800x300')
message = StringVar()

message_entry = Entry(textvariable=message,width=52)
message_entry.place(relx=.3, rely=.1, anchor='c')