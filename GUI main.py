import tkinter as tk
import tkinter.font as tf
from tkinter.ttk import*
from PIL import Image, ImageTk
from Board import Board

root = tk.Tk()
root.geometry()
root.title("TIC TAC TOE")


root.geometry('600x350+600+300')
root.config(bg='black')
frame19 = tk.Frame(root)
frameXO = tk.Frame(root)

frame19.grid(column=0, row=0, padx=50, pady=50)
frameXO.grid(column=2, row=0)

image_o = Image.open('c:/Users/stefan.gal/Documents/Python/GithubForks/Tictactoe/img/O.jpg')
image_x = Image.open('c:/Users/stefan.gal/Documents/Python/GithubForks/Tictactoe/img/X.jpg')
image_e = Image.open('c:/Users/stefan.gal/Documents/Python/GithubForks/Tictactoe/img/empty.jpg')

image_o = image_o.resize((70, 70), Image.ANTIALIAS)
image_x = image_x.resize((70, 70), Image.ANTIALIAS)
image_e = image_e.resize((70, 70), Image.ANTIALIAS)

photo_o = ImageTk.PhotoImage(image_o)
photo_x = ImageTk.PhotoImage(image_x)
photo_e = ImageTk.PhotoImage(image_e)

global x
x = 1

def click1():
    global x
    lst = [photo_x, photo_o]
    return button1.config(image=lst[x],width=70, height=70)

def click2():
    global x
    lst = [photo_x, photo_o]
    return button2.config(image=lst[x],width=70, height=70)

def click3():
    global x
    lst = [photo_x, photo_o]
    return button3.config(image=lst[x],width=70, height=70)

def click4():
    global x
    lst = [photo_x, photo_o]
    return button4.config(image=lst[x],width=70, height=70)

def click5():
    global x
    lst = [photo_x, photo_o]
    return button5.config(image=lst[x],width=70, height=70)

def click6():
    global x
    lst = [photo_x, photo_o]
    return button6.config(image=lst[x],width=70, height=70)

def click7():
    global x
    lst = [photo_x, photo_o]
    return button7.config(image=lst[x],width=70, height=70)

def click8():
    global x
    lst = [photo_x, photo_o]
    return button8.config(image=lst[x],width=70, height=70)

def click9():
    global x
    lst = [photo_x, photo_o]
    return button9.config(image=lst[x],width=70, height=70)


# 1 - 9 BUTTONS
button1 = tk.Button(frame19, command=click1, image=photo_e, width=70, height=70, bg='white', fg='red')
button1.grid(column=0, row=0)
button2 = tk.Button(frame19, command=click2, image=photo_e, bg='white', fg='red')
button2.grid(column=1, row=0)
button3 = tk.Button(frame19, command=click3, image=photo_e, bg='white', fg='red')
button3.grid(column=2, row=0)
button4 = tk.Button(frame19, command=click4, image=photo_e, bg='white', fg='red')
button4.grid(column=0, row=1)
button5 = tk.Button(frame19, command=click5, image=photo_e, bg='white', fg='red')
button5.grid(column=1, row=1)
button6 = tk.Button(frame19, command=click6, image=photo_e, bg='white', fg='red')
button6.grid(column=2, row=1)
button7 = tk.Button(frame19, command=click7, image=photo_e, bg='white', fg='red')
button7.grid(column=0, row=2)
button8 = tk.Button(frame19, command=click8, image=photo_e, bg='white', fg='red')
button8.grid(column=1, row=2)
button9 = tk.Button(frame19, command=click9, image=photo_e,bg='white', fg='red')
button9.grid(column=2, row=2)

#  X - O BUTTONS
buttonX = tk.Button(frameXO, image=photo_x, bg='white', fg='red')
buttonO = tk.Button(frameXO, image=photo_o, bg='white', fg='red')
buttonX.grid(column=4, row=0)
buttonO.grid(column=5, row=0)



#MARKINGS
# def markings(pos, xo):
#     bt = 'button'+pos
#     ph = 'photo_'+xo
#     return globals()[bt].config(image=globals()[ph])

# markings('3', 'x')
# markings('2', 'x')


root.mainloop()
