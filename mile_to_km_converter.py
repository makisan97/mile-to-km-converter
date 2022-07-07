from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=100)
window.config(padx=20, pady=20)


def button_clicked():
    miles = float(input_miles.get())
    label_4.config(text=round(miles * 1.60934, 5))


label_1 = Label(text="Miles", font="bold")
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to", font="bold")
label_2.grid(row=1, column=0)

label_3 = Label(text="Km", font="bold")
label_3.grid(row=1, column=2)

label_4 = Label(text=0, font="bold")
label_4.grid(row=1, column=1)

input_miles = Entry(width=10)
input_miles.grid(row=0, column=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()
