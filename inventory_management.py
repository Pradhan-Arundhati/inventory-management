from tkinter import *
import tkinter as tk
from tkinter import Label
from tkinter import messagebox

window = Tk()
window.resizable(True, True)
window.geometry('900x450')
window.title("*****INVENTORY MANAGEMENT*****")

line = LabelFrame(window, text="INVENTORY MANAGEMENT")
line.pack(fill="both", expand="yes")

Information = Label(window, text="Product Details", font=("Arial", 10)).place(x=250, y=1)

product_id = Label(window, text="Product Id: ", font=("Arial Bold", 10)).place(x=20, y=50)
input_one = Entry(window, width=16)
input_one.place(x=20, y=80)

product_name = Label(window, text="Product Name: ", font=("Arial Bold", 10)).place(x=20, y=120)
input_two = Entry(window, width=16)
input_two.place(x=20, y=150)

selling_price = Label(window, text="Selling Price: ", font=("Arial Bold", 10)).place(x=20, y=190)
input_three = Entry(window, width=16)
input_three.place(x=20, y=220)

quantity = Label(window, text="Quantity: ", font=("Arial Bold", 10)).place(x=20, y=260)
input_four = Entry(window, width=16)
input_four.place(x=20, y=290)

info_item_no = Label(window, text="Item no", relief="raised", font=("Arial ", 15)).place(x=200, y=40)
info_product_id = Label(window, text="Product Id", relief="raised", font=("Arial ", 15)).place(x=320, y=40)
info_product_name = Label(window, text="Product Name", relief="raised", font=("Arial ", 15)).place(x=450, y=40)
info_selling_price = Label(window, text="Selling Price", relief="raised", font=("Arial ", 15)).place(x=620, y=40)
info_quantity = Label(window, text="Quantity", relief="raised", font=("Arial ", 15)).place(x=765, y=40)

text = Text(window, height=20, width=80)
text.place(x=200, y=70)


def inserting_details():
    write_product_id = str(input_one.get())
    write_product_name = str(input_two.get())
    write_selling_price = str(input_three.get())
    write_quantity = str(input_four.get())
    check = open('details.txt', 'a')
    check1 = open('details.txt', 'r')
    test = check1.read()
    if write_product_id in test:
        messagebox.showerror("Duplicate", "Number already exist")
    else:
        check1 = open("details.txt", 'r')
        count = len(check1.readlines())
        check1 = open("details.txt", 'a')
        item_no = str(count+1)
        check1.write(f"{item_no}\t\t   {write_product_id}\t\t  {write_product_name}\t\t     \t{write_selling_price}\t    \t{write_quantity}\n")
        messagebox.showinfo("Information", "Data added successfully")

    input_one.delete(0, tk.END)
    input_two.delete(0, tk.END)
    input_three.delete(0, tk.END)
    input_four.delete(0, tk.END)


def show_details():
    text.delete(0.0, END)
    check = open('details.txt', 'r')
    rest = check.read()
    for a in rest[::-1]:
        text.insert(0.0, a)


def clear_details():
    text.delete(0.0, tk.END)


def exit_frame():
    window.destroy()


insert_button = Button(window, text="Insert", command=inserting_details, height=2, width=5, font=("Arial Bold", 10), bg="lightblue").place(x=20, y=320)
show_button = Button(window, text="show", command=show_details, height=2, width=5, font=("Arial Bold", 10), bg="lightblue").place(x=100, y=320)
clear_button = Button(window, text="clear", command=clear_details, height=2, width=5, font=("Arial Bold", 10), bg="lightblue").place(x=20, y=380)
exit_button = Button(window, text="Exit", command=exit_frame, height=2, width=5, font=("Arial Bold", 10), bg="lightblue").place(x=100, y=380)

window.mainloop()
