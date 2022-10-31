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



#Viernes
viernes1 = Frame(root)
viernes1.config(bg = "green", width = 100, height = 100)
viernes1.grid(row = 1, column = 4)

viernes2 = Frame(root)
viernes2.config(bg = "green", width = 100, height = 100)
viernes2.grid(row = 2, column = 4)

viernes3 = Frame(root)
viernes3.config(bg = "green", width = 100, height = 100)
viernes3.grid(row = 3, column = 4)

viernes4 = Frame(root)
viernes4.config(bg = "green", width = 100, height = 100)
viernes4.grid(row = 4, column = 4)

viernes5 = Frame(root)
viernes5.config(bg = "green", width = 100, height = 100)
viernes5.grid(row = 5, column = 4)

viernes6 = Frame(root)
viernes6.config(bg = "green", width = 100, height = 100)
viernes6.grid(row = 6, column = 4)



#Sábado
sabado1 = Frame(root)
sabado1.config(bg = "darkgreen", width = 100, height = 100)
sabado1.grid(row = 1, column = 5)

sabado2 = Frame(root)
sabado2.config(bg = "darkgreen", width = 100, height = 100)
sabado2.grid(row = 2, column = 5)

sabado3 = Frame(root)
sabado3.config(bg = "darkgreen", width = 100, height = 100)
sabado3.grid(row = 3, column = 5)

sabado4 = Frame(root)
sabado4.config(bg = "darkgreen", width = 100, height = 100)
sabado4.grid(row = 4, column = 5)

sabado5 = Frame(root)
sabado5.config(bg = "darkgreen", width = 100, height = 100)
sabado5.grid(row = 5, column = 5)

sabado6 = Frame(root)
sabado6.config(bg = "darkgreen", width = 100, height = 100)
sabado6.grid(row = 6, column = 5)

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

viernes = Frame(root)
textoV = Label(root, text = "Viernes", bg = "green", font = ("Arial",14)).grid(row = 0, column = 4)
viernes.config(bg = "green", width = 100, height = 30)
viernes.grid(row = 0, column =4)

sabado = Frame(root)
textoV = Label(root, text = "Sábado", bg = "darkgreen", font = ("Arial",14)).grid(row = 0, column = 5)
sabado.config(bg = "darkgreen", width = 100, height = 30)
sabado.grid(row = 0, column =5)

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

# Botones Viernes

botonV1 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=1, column=4)

botonV2 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=2, column=4)

botonV3 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=3, column=4)

botonV4 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=4, column=4)

botonV5 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=5, column=4)

botonV6 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=6, column=4)

# Botones Sabado

botonS1 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=1, column=5)

botonS2 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=2, column=5)

botonS3 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=3, column=5)

botonS4 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=4, column=5)

botonS5 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=5, column=5)

botonS6 = Button(root, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=6, column=5)

root.mainloop()
