from tkinter import *
root = Tk()
#Lunes
lunes = Frame(root)
lunes.config(bg = "red", width = 100, height = 600)
lunes.grid(row = 0, column = 0)
#Martes
martes = Frame(root)
martes.config(bg = "lightblue", width = 100, height = 600)
martes.grid(row = 0, column = 1)
#Miércoles
miercoles = Frame(root)
miercoles.config(bg = "orange", width = 100, height = 600)
miercoles.grid(row = 0, column = 2)
#Jueves
jueves = Frame(root)
jueves.config(bg = "yellow", width = 100, height = 600)
jueves.grid(row = 0, column = 3)
#Viernes
viernes = Frame(root)
viernes.config(bg = "green", width = 100, height = 600)
viernes.grid(row = 0, column = 4)
#Sábado
sabado = Frame(root)
sabado.config(bg = "darkgreen", width = 100, height = 600)
sabado.grid(row = 0, column = 5)
