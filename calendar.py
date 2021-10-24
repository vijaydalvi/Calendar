from tkinter import *
import calendar

text = calendar.calendar(2021)
root = Tk()
root.geometry("500x650")
root.title("CALENDAR  Develop Vijay Dalvi")
root.resizable(0, 0)
label1 = Label(root, text="CALENDER", bg='dark gray', font=("time", 28, 'bold'))
label1.grid(row=1, column=1)
root.config(background="white")
l1 = Label(root, text=text, font="Consolas 8")
l1.grid(row=2, column=1, padx=20)
root.mainloop()
