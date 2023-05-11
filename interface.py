from tkinter import *
from main import Orange
from main import Pear
from main import Grape
from main import Guava
from main import Sub_orange


# Digitando valor de saída/entrada do item laranja 
def Laranja():
    # Adicionando
    Label(app, text="Laranja", background="#fff", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
    add_laranja = Entry(app)
    add_laranja.place(x=10, y=50, width=200, height=20)
    Button(app, text="Enviar", command=lambda:Orange(add_laranja)).place(x=10, y=270, width=100,height=20)

    # Subtraindo 
    Label(app, text="Subtrair Laranja", background="#fff", foreground="#009", anchor=W).place(x=20, y=20, width=100, height=20)
    sub_laranja = Entry(app)
    sub_laranja.place(x=20, y=60, width=200, height=20)
    Button(app, text="send", command=lambda:Sub_orange(sub_laranja)).place(x=40, y=30, width=100,height=40)

# Digitando valor de saída/entrada do item pêra 
def Pera():
    Label(app, text="Pêra", background="#fff", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
    add_pera = Entry(app)
    add_pera.place(x=10, y=50, width=200, height=20)

    Button(app, text="Enviar", command=lambda:Pear(add_pera)).place(x=10, y=270, width=100,height=20)


# Digitando valor de saída/entrada do item Uva 
def Uva():
    Label(app, text="Uva", background="#fff", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
    add_uva = Entry(app)
    add_uva.place(x=10, y=50, width=200, height=20)

    Button(app, text="Enviar", command=lambda:Grape(add_uva)).place(x=10, y=270, width=100,height=20)


# Digitando valor de saída/entrada do item Goiaba 
def Goiaba():
    Label(app, text="Goiaba", background="#fff", foreground="#009", anchor=W).place(x=10, y=10, width=100, height=20)
    add_goiaba = Entry(app)
    add_goiaba.place(x=10, y=50, width=200, height=20)

    Button(app, text="Enviar", command=lambda:Guava(add_goiaba)).place(x=10, y=270, width=100,height=20)

app = Tk()
app.title("Sales App")
app.geometry("500x300")
app.configure(background="#dde") 

# Criando barra de menu
barra_menu = Menu(app)
menu_frutas = Menu(barra_menu, tearoff = 0)
menu_frutas.add_command(label = "Laranja", command = Laranja)
menu_frutas.add_command(label = "Pera", command = Pera)
menu_frutas.add_command(label = "Uva", command = Uva)
menu_frutas.add_command(label = "Goiaba", command = Goiaba)


barra_menu.add_cascade(label = "Frutas", menu = menu_frutas)


app.config(menu=barra_menu)
app.mainloop()