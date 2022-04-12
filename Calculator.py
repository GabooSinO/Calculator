from tkinter import *

ventana = Tk()
ventana.geometry("310x410")
ventana.title("Calculadora")

i = 0
b = 0

e_texto = Entry(ventana, font = ("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

#-----------------------------FUNCIONES-----------------------------------------

def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrarTodo():
    e_texto.delete(0, END)

def operaciones():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto. insert(0, resultado)
    i = 0
#-----------------------------BUTTONS-------------------------------------------

boton1 = Button(ventana, text = "1", width = 8, height = 4, command = lambda: click_boton(1))
boton2 = Button(ventana, text = "2", width = 8, height = 4, command = lambda: click_boton(2))
boton3 = Button(ventana, text = "3", width = 8, height = 4, command = lambda: click_boton(3))
boton4 = Button(ventana, text = "4", width = 8, height = 4, command = lambda: click_boton(4))
boton5 = Button(ventana, text = "5", width = 8, height = 4, command = lambda: click_boton(5))
boton6 = Button(ventana, text = "6", width = 8, height = 4, command = lambda: click_boton(6))
boton7 = Button(ventana, text = "7", width = 8, height = 4, command = lambda: click_boton(7))
boton8 = Button(ventana, text = "8", width = 8, height = 4, command = lambda: click_boton(8))
boton9 = Button(ventana, text = "9", width = 8, height = 4, command = lambda: click_boton(9))
boton0 = Button(ventana, text = "0", width = 8, height = 4, command = lambda: click_boton(0))
botonIgual =            Button(ventana, text = "=", width = 8, height = 4, command = lambda: operaciones())
botonSuma =             Button(ventana, text = "+", width = 8, height = 4, command = lambda: click_boton("+"))
botonResta =            Button(ventana, text = "-", width = 8, height = 4, command = lambda: click_boton("-"))
botonMultiplicacion =   Button(ventana, text = "*", width = 8, height = 4, command = lambda: click_boton("*"))
botonDivision =         Button(ventana, text = "/", width = 8, height = 4, command = lambda: click_boton("/"))
botonPunto =             Button(ventana, text = ".", width = 8, height = 4, command = lambda: click_boton("."))
botonMasMenos =         Button(ventana, text = "+/-", width = 8, height = 4, command = lambda: click_boton("-"))
botonBorrar =           Button(ventana, text = "<-", width = 8, height = 4, command = lambda: borrarTodo())
botonBorrarTodo =       Button(ventana, text = "C", width = 8, height = 4, command = lambda: borrarTodo())

boton1.grid(row = 4, column = 0)
boton2.grid(row = 4, column = 1)
boton3.grid(row = 4, column = 2)
boton4.grid(row = 3, column = 0)
boton5.grid(row = 3, column = 1)
boton6.grid(row = 3, column = 2)
boton7.grid(row = 2, column = 0)
boton8.grid(row = 2, column = 1)
boton9.grid(row = 2, column = 2)
boton0.grid(row = 5, column = 1)
botonMasMenos.grid(row = 5, column = 0)
botonPunto.grid(row = 5, column = 2)
botonIgual.grid(row = 5, column = 3)
botonSuma.grid(row = 4, column = 3)
botonResta.grid(row = 3, column = 3)
botonMultiplicacion.grid(row = 2, column = 3)
botonDivision.grid(row = 1, column = 3)
botonBorrar.grid(row = 1, column = 2)
botonBorrarTodo.grid(row = 1, column = 1)

ventana.mainloop()
