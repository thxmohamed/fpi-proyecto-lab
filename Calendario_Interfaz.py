from tkinter import *
root = Tk()

#Lunes
lunes1 = Frame(root)
lunes1.config(bg = "red", width = 100, height = 100)
lunes1.grid(row = 1, column = 0)

lunes2 = Frame(root)
lunes2.config(bg = "red", width = 100, height = 100)
lunes2.grid(row = 2, column = 0)

lunes3 = Frame(root)
lunes3.config(bg = "red", width = 100, height = 100)
lunes3.grid(row = 3, column = 0)

lunes4 = Frame(root)
lunes4.config(bg = "red", width = 100, height = 100)
lunes4.grid(row = 4, column = 0)

lunes5 = Frame(root)
lunes5.config(bg = "red", width = 100, height = 100)
lunes5.grid(row = 5, column = 0)

lunes6 = Frame(root)
lunes6.config(bg = "red", width = 100, height = 100)
lunes6.grid(row = 6, column = 0)


#Martes
martes1 = Frame(root)
martes1.config(bg = "lightblue", width = 100, height = 100)
martes1.grid(row = 1, column = 1)

martes2 = Frame(root)
martes2.config(bg = "lightblue", width = 100, height = 100)
martes2.grid(row = 2, column = 1)

martes3 = Frame(root)
martes3.config(bg = "lightblue", width = 100, height = 100)
martes3.grid(row = 3, column = 1)

martes4 = Frame(root)
martes4.config(bg = "lightblue", width = 100, height = 100)
martes4.grid(row = 4, column = 1)

martes5 = Frame(root)
martes5.config(bg = "lightblue", width = 100, height = 100)
martes5.grid(row = 5, column = 1)

martes6 = Frame(root)
martes6.config(bg = "lightblue", width = 100, height = 100)
martes6.grid(row = 6, column = 1)


#Miércoles
miercoles1 = Frame(root)
miercoles1.config(bg = "orange", width = 100, height = 100)
miercoles1.grid(row = 1, column = 2)

miercoles2 = Frame(root)
miercoles2.config(bg = "orange", width = 100, height = 100)
miercoles2.grid(row = 2, column = 2)

miercoles3 = Frame(root)
miercoles3.config(bg = "orange", width = 100, height = 100)
miercoles3.grid(row = 3, column = 2)

miercoles4 = Frame(root)
miercoles4.config(bg = "orange", width = 100, height = 100)
miercoles4.grid(row = 4, column = 2)

miercoles5 = Frame(root)
miercoles5.config(bg = "orange", width = 100, height = 100)
miercoles5.grid(row = 5, column = 2)

miercoles = Frame(root)
miercoles.config(bg = "orange", width = 100, height = 100)
miercoles.grid(row = 6, column = 2)


#Jueves
jueves1 = Frame(root)
jueves1.config(bg = "yellow", width = 100, height = 100)
jueves1.grid(row = 1, column = 3)

jueves2 = Frame(root)
jueves2.config(bg = "yellow", width = 100, height = 100)
jueves2.grid(row = 2, column = 3)

jueves3 = Frame(root)
jueves3.config(bg = "yellow", width = 100, height = 100)
jueves3.grid(row = 3, column = 3)

jueves4 = Frame(root)
jueves4.config(bg = "yellow", width = 100, height = 100)
jueves4.grid(row = 4, column = 3)

jueves5 = Frame(root)
jueves5.config(bg = "yellow", width = 100, height = 100)
jueves5.grid(row = 5, column = 3)

jueves6 = Frame(root)
jueves6.config(bg = "yellow", width = 100, height = 100)
jueves6.grid(row = 6, column = 3)


'''
#Viernes
viernes = Frame(root)
viernes.config(bg = "green", width = 100, height = 600)
viernes.grid(row = 0, column = 4)
#Sábado
sabado = Frame(root)
sabado.config(bg = "darkgreen", width = 100, height = 600)
sabado.grid(row = 0, column = 5)
'''

#Asignación de días


lunes = Frame(root)
textoL = Label(root, text = "Lunes", bg = "red", font = ("Arial",14)).grid(row = 0, column = 0)
lunes.config(bg = "red", width = 100, height =  30)
lunes.grid(row = 0, column = 0)

martes = Frame(root)
textoM = Label(root, text = "Martes", bg = "lightblue", font = ("Arial",14)).grid(row = 0, column = 1)
martes.config(bg = "lightblue", width = 100, height = 30)
martes.grid(row = 0, column =1)

miercoles = Frame(root)
textoW = Label(root, text = "Miércoles", bg = "orange", font = ("Arial",14)).grid(row = 0, column = 2)
miercoles.config(bg = "orange", width = 100, height = 30)
miercoles.grid(row = 0, column =2)

jueves = Frame(root)
textoJ = Label(root, text = "Jueves", bg = "yellow", font = ("Arial",14)).grid(row = 0, column = 3)
jueves.config(bg = "yellow", width = 100, height = 30)
jueves.grid(row = 0, column =3)

#Botones Lunes

botonL1 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=1, column=0)

botonL2 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=2, column=0)

botonL3 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=3, column=0)

botonL4 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=4, column=0)

botonL5 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=5, column=0)

botonL6 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=6, column=0)

#Botones Martes

botonM1 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=1, column=1)

botonM2 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=2, column=1)

botonM3 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=3, column=1)

botonM4 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=4, column=1)

botonM5 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=5, column=1)

botonM6 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=6, column=1)


# Botones Miercoles 
botonW1 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=1, column=2)

botonW2 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=2, column=2)

botonW3 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=3, column=2)

botonW4 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=4, column=2)

botonW5 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=5, column=2)

botonW6 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=6, column=2)

# Botones Jueves

botonJ1 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=1, column=3)

botonJ2 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=2, column=3)

botonJ3 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=3, column=3)

botonJ4 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=4, column=3)

botonJ5 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=5, column=3)

botonJ6 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=6, column=3)

root.mainloop()
