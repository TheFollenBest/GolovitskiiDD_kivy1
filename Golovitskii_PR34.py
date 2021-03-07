from tkinter import *
from tkinter import messagebox
import pickle

backgroundColor = "#82E5A8"


def registration_form():
    tk.destroy()
    ak = Tk()
    ak.title("Регистрация")
    ak.geometry("450x425")

    def clear():
        name.delete(0, END)
        surname.delete(0, END)

    ak.configure(background=backgroundColor)

    caption = Label(text="Регистрация", font=("Bahnschrift", 14), background="#82E5A8", foreground="#000000")
    caption.place(x=225, y=50,  height=30, width=220, anchor="c",  bordermode=OUTSIDE)

    name = Entry(ak, bd=0, font=("Bahnschrift", 12),  foreground="#E5E5E5")
    name.place(x=225, y=100, height=30, width=230, anchor="c",  bordermode=OUTSIDE)

    surname = Entry(ak, bd=0, font=("Bahnschrift", 12),  foreground="#E5E5E5")
    surname.place(x=225, y=150, height=30, width=230, anchor="c",  bordermode=OUTSIDE)

    login = Entry(ak, bd=0, font=("Bahnschrift", 12),  foreground="#E5E5E5")
    login.place(x=225, y=200, height=30, width=230, anchor="c",  bordermode=OUTSIDE)

    password = Entry(ak, bd=0, font=("Bahnschrift", 12),  foreground="#E5E5E5")
    password.place(x=225, y=250, height=30, width=230, anchor="c",  bordermode=OUTSIDE)

    repeat_password = Entry(ak, bd=0, font=("Bahnschrift", 12),  foreground="#E5E5E5")
    repeat_password.place(x=225, y=300, height=30, width=230, anchor="c",  bordermode=OUTSIDE)

    name.insert(0, "Имя")
    surname.insert(0, "Фамилия")
    login.insert(0, "Логин")
    password.insert(0, "Пароль")
    repeat_password.insert(0, "Повторите пароль")

    def test():
        if len(name.get()) == 0 or len(surname.get()) == 0 or len(login.get()) == 0 or len(password.get()) == 0 or len(repeat_password.get()) == 0:
            messagebox.showerror("Ошибка", "Не все поля введены!")
        if password.get() != repeat_password.get():
            messagebox.showerror("Ошибка", "Пароли не совпадают!")
        if len(password.get()) < 8:
            messagebox.showerror("Ошибка", "Пароль должен содержать 8 символов!")

    button_registration = Button(ak, text="Регистрация", background="#1FAF8C", foreground="#ffffff", font=("Bahnschrift", 12, "bold"), border=0, command=lambda: test())
    button_registration.place(x=225, y=350, height=30, width=230, anchor="c", bordermode=OUTSIDE)


tk = Tk()
tk.title("Вход")
tk.geometry("450x325")
tk.configure(background=backgroundColor)

caption = Label(text="Вход", font=("Bahnschrift", 16), background="#82E5A8", foreground="#000000")
caption.place(x=225, y=50,  height=30, width=230, anchor="c",  bordermode=OUTSIDE)

login = Entry(tk, bd=0, font=("Bahnschrift", 12), foreground="#E5E5E5")
login.place(x=225, y=100, height=30, width=230, anchor="c",  bordermode=OUTSIDE)

password = Entry(tk, bd=0, font=("Bahnschrift", 12),  foreground="#E5E5E5")
password.place(x=225, y=150, height=30, width=230, anchor="c",  bordermode=OUTSIDE)

button_entrance = Button(tk, text="Вход",  background="#1FAF8C", foreground="#FFF", font=("Bahnschrift", 12, "bold"), border=0, command=lambda: test())
button_entrance.place(x=225, y=200, height=30, width=230,  anchor="c", bordermode=OUTSIDE)

button_registration_main = Button(tk, text="Регистрация", background="#1FAF8C", foreground="#FFF", font=("Bahnschrift", 12, "bold"), border=0, command=registration_form)
button_registration_main.place(x=225, y=250, height=30, width=230, anchor="c", bordermode=OUTSIDE)

login.insert(0, "Логин")
password.insert(0, "Пароль")


def test():
    if len(password.get()) == 0 or len(password.get()) == 0:
        messagebox.showerror("Ошибка", "Не все поля введены!")


ismarried = IntVar()
ismarried_checkbutton = Checkbutton(text="Запомнить пароль", font=("Bahnschrift", 12),  foreground="#545863", background="#82E5A8", variable=ismarried)
ismarried_checkbutton.place(x=150, y=300, height=30, width=275, anchor="s", bordermode=OUTSIDE)

text_enter_password = Label(text="Забыли пароль?", font=("Bahnschrift", 12), background="#82E5A8", foreground="#545863")
text_enter_password.place(x=325, y=300, height=30, width=175, anchor="s", bordermode=OUTSIDE)


tk.mainloop()
