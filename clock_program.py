from tkinter import*
from time import*


def update():
    time_string = strftime("%I:%M:%S, %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()

window.title("Digital Clock")

time_label = Label(window, font=("arial", 80), fg='red', bg='black')
time_label.pack()

day_label = Label(window, font=("monospaced", 30), fg='black', bg='yellow')
day_label.pack()

date_label = Label(window, font=("times new roman", 35), fg='green', bg='white')
date_label.pack()

update()


window.mainloop()
