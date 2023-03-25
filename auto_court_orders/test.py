import tkinter as tk

from datetime import datetime


def clock():
    clock_window = tk.Toplevel()
    clock_window.title("Часы")
    label = tk.Label(clock_window, font=("helvetica", 40))
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def update_time():
        clock_window.geometry('270x450+{}+{}'.format(500, 400))
        label.config(text=f"{datetime.now():%H:%M:%S}")
        clock_window.after(100, update_time)  # Запланировать выполнение этой же функции через 100 миллисекунд

    update_time()


window = tk.Tk()
window.geometry('270x450')

button_1 = tk.Button(text='Часы', width=10, height=5, font=('Roman 10'), command=clock)
button_1.place(x=50, y=50)

button_2 = tk.Button(text='Календарь', width=12, height=6, font=('Roman 8'))
button_2.place(x=150, y=50)

button_3 = tk.Button(text='Настройки', width=10, height=5, font=('Roman 9'))
button_3.place(x=50, y=150)

button_4 = tk.Button(text='Игра', width=10, height=5, font=('Roman 10'))
button_4.place(x=150, y=150)

window.mainloop()