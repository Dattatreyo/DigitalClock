from customtkinter import *

from time import strftime

app = CTk()
app.geometry('500x300')
app.title('Digital Clock')

tabview = CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

tabview.add("12hr format")
tabview.add("24hr format")


def twelve():
    string1 = strftime('%I:%M:%S %p')

    label_1.configure(text=string1)

    label_1.after(1000, twelve)


def twenty():
    string2 = strftime('%H:%M:%S %p')
    label_2.configure(text=string2)
    label_2.after(1000, twenty)


label_1 = CTkLabel(master=tabview.tab("12hr format"), fg_color="Black", bg_color="cyan", font=("ds-digital", 80))
label_1.pack(padx=20, pady=20)
twelve()

label_2 = CTkLabel(master=tabview.tab("24hr format"), fg_color="red", bg_color="black", font=("ds-digital", 80))
label_2.pack(padx=20, pady=20)
twenty()

app.mainloop()
