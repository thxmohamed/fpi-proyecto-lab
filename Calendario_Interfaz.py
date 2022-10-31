from tkinter import *
root = Tk()
#Ventana de entrada de actividades
def ventana_entra_act():
    ventana_entrada=Toplevel()
    ventana_entrada.title("ventana secundaria")
    ventana_entrada.geometry("100x50")
    entrada=Entry(ventana_entrada)
    entrada.insert(0,"ingrsa actividad")
    entrada.grid(row=0)
    def boton_enviar():
        botonL1.config(text=entrada.get())
    boton_enviar=Button(ventana_entrada,text="guardar",command=boton_enviar,bg="red")
    boton_enviar.grid(row=1)
    #boton1.config(text=alo)
#Ventana del calendario
def cambia_ventana():
    ventana_nueva=Toplevel()
    ventana_nueva.title("ventana secundaria")
    ventana_nueva.geometry("900x900")
    etiqueta=Label(ventana_nueva,text="olas")
    #Lunes
    lunes1 = Frame(ventana_nueva)
    lunes1.config(bg = "red", width = 100, height = 100)
    lunes1.grid(row = 1, column = 0)


    lunes2 = Frame(ventana_nueva)
    lunes2.config(bg = "red", width = 100, height = 100)
    lunes2.grid(row = 2, column = 0)

    lunes3 = Frame(ventana_nueva)
    lunes3.config(bg = "red", width = 100, height = 100)
    lunes3.grid(row = 3, column = 0)

    lunes4 = Frame(ventana_nueva)
    lunes4.config(bg = "red", width = 100, height = 100)
    lunes4.grid(row = 4, column = 0)

    lunes5 = Frame(ventana_nueva)
    lunes5.config(bg = "red", width = 100, height = 100)
    lunes5.grid(row = 5, column = 0)

    lunes6 = Frame(ventana_nueva)
    lunes6.config(bg = "red", width = 100, height = 100)
    lunes6.grid(row = 6, column = 0)


    #Martes
    martes1 = Frame(ventana_nueva)
    martes1.config(bg = "lightblue", width = 100, height = 100)
    martes1.grid(row = 1, column = 1)

    martes2 = Frame(ventana_nueva)
    martes2.config(bg = "lightblue", width = 100, height = 100)
    martes2.grid(row = 2, column = 1)

    martes3 = Frame(ventana_nueva)
    martes3.config(bg = "lightblue", width = 100, height = 100)
    martes3.grid(row = 3, column = 1)

    martes4 = Frame(ventana_nueva)
    martes4.config(bg = "lightblue", width = 100, height = 100)
    martes4.grid(row = 4, column = 1)

    martes5 = Frame(ventana_nueva)
    martes5.config(bg = "lightblue", width = 100, height = 100)
    martes5.grid(row = 5, column = 1)

    martes6 = Frame(ventana_nueva)
    martes6.config(bg = "lightblue", width = 100, height = 100)
    martes6.grid(row = 6, column = 1)


    #Miércoles
    miercoles1 = Frame(ventana_nueva)
    miercoles1.config(bg = "orange", width = 100, height = 100)
    miercoles1.grid(row = 1, column = 2)

    miercoles2 = Frame(ventana_nueva)
    miercoles2.config(bg = "orange", width = 100, height = 100)
    miercoles2.grid(row = 2, column = 2)

    miercoles3 = Frame(ventana_nueva)
    miercoles3.config(bg = "orange", width = 100, height = 100)
    miercoles3.grid(row = 3, column = 2)

    miercoles4 = Frame(ventana_nueva)
    miercoles4.config(bg = "orange", width = 100, height = 100)
    miercoles4.grid(row = 4, column = 2)

    miercoles5 = Frame(ventana_nueva)
    miercoles5.config(bg = "orange", width = 100, height = 100)
    miercoles5.grid(row = 5, column = 2)

    miercoles = Frame(ventana_nueva)
    miercoles.config(bg = "orange", width = 100, height = 100)
    miercoles.grid(row = 6, column = 2)


    #Jueves
    jueves1 = Frame(ventana_nueva)
    jueves1.config(bg = "yellow", width = 100, height = 100)
    jueves1.grid(row = 1, column = 3)

    jueves2 = Frame(ventana_nueva)
    jueves2.config(bg = "yellow", width = 100, height = 100)
    jueves2.grid(row = 2, column = 3)

    jueves3 = Frame(ventana_nueva)
    jueves3.config(bg = "yellow", width = 100, height = 100)
    jueves3.grid(row = 3, column = 3)

    jueves4 = Frame(ventana_nueva)
    jueves4.config(bg = "yellow", width = 100, height = 100)
    jueves4.grid(row = 4, column = 3)

    jueves5 = Frame(ventana_nueva)
    jueves5.config(bg = "yellow", width = 100, height = 100)
    jueves5.grid(row = 5, column = 3)

    jueves6 = Frame(ventana_nueva)
    jueves6.config(bg = "yellow", width = 100, height = 100)
    jueves6.grid(row = 6, column = 3)



    #Viernes
    viernes1 = Frame(ventana_nueva)
    viernes1.config(bg = "green", width = 100, height = 100)
    viernes1.grid(row = 1, column = 4)

    viernes2 = Frame(ventana_nueva)
    viernes2.config(bg = "green", width = 100, height = 100)
    viernes2.grid(row = 2, column = 4)

    viernes3 = Frame(ventana_nueva)
    viernes3.config(bg = "green", width = 100, height = 100)
    viernes3.grid(row = 3, column = 4)

    viernes4 = Frame(ventana_nueva)
    viernes4.config(bg = "green", width = 100, height = 100)
    viernes4.grid(row = 4, column = 4)

    viernes5 = Frame(ventana_nueva)
    viernes5.config(bg = "green", width = 100, height = 100)
    viernes5.grid(row = 5, column = 4)

    viernes6 = Frame(ventana_nueva)
    viernes6.config(bg = "green", width = 100, height = 100)
    viernes6.grid(row = 6, column = 4)



    #Sábado
    sabado1 = Frame(ventana_nueva)
    sabado1.config(bg = "darkgreen", width = 100, height = 100)
    sabado1.grid(row = 1, column = 5)

    sabado2 = Frame(ventana_nueva)
    sabado2.config(bg = "darkgreen", width = 100, height = 100)
    sabado2.grid(row = 2, column = 5)

    sabado3 = Frame(ventana_nueva)
    sabado3.config(bg = "darkgreen", width = 100, height = 100)
    sabado3.grid(row = 3, column = 5)

    sabado4 = Frame(ventana_nueva)
    sabado4.config(bg = "darkgreen", width = 100, height = 100)
    sabado4.grid(row = 4, column = 5)

    sabado5 = Frame(ventana_nueva)
    sabado5.config(bg = "darkgreen", width = 100, height = 100)
    sabado5.grid(row = 5, column = 5)

    sabado6 = Frame(ventana_nueva)
    sabado6.config(bg = "darkgreen", width = 100, height = 100)
    sabado6.grid(row = 6, column = 5)

    #Asignación de días


    lunes = Frame(ventana_nueva)
    textoL = Label(ventana_nueva, text = "Lunes", bg = "red", font = ("Arial",14)).grid(row = 0, column = 0)
    lunes.config(bg = "red", width = 100, height =  30)
    lunes.grid(row = 0, column = 0)

    martes = Frame(ventana_nueva)
    textoM = Label(ventana_nueva, text = "Martes", bg = "lightblue", font = ("Arial",14)).grid(row = 0, column = 1)
    martes.config(bg = "lightblue", width = 100, height = 30)
    martes.grid(row = 0, column =1)

    miercoles = Frame(ventana_nueva)
    textoW = Label(ventana_nueva, text = "Miércoles", bg = "orange", font = ("Arial",14)).grid(row = 0, column = 2)
    miercoles.config(bg = "orange", width = 100, height = 30)
    miercoles.grid(row = 0, column =2)

    jueves = Frame(ventana_nueva)
    textoJ = Label(ventana_nueva, text = "Jueves", bg = "yellow", font = ("Arial",14)).grid(row = 0, column = 3)
    jueves.config(bg = "yellow", width = 100, height = 30)
    jueves.grid(row = 0, column =3)

    viernes = Frame(ventana_nueva)
    textoV = Label(ventana_nueva, text = "Viernes", bg = "green", font = ("Arial",14)).grid(row = 0, column = 4)
    viernes.config(bg = "green", width = 100, height = 30)
    viernes.grid(row = 0, column =4)

    sabado = Frame(ventana_nueva)
    textoV = Label(ventana_nueva, text = "Sábado", bg = "darkgreen", font = ("Arial",14)).grid(row = 0, column = 5)
    sabado.config(bg = "darkgreen", width = 100, height = 30)
    sabado.grid(row = 0, column =5)

    #Botones Lunes
    """
    def ventana_entra_act():
        ventana_entrada=Toplevel()
        ventana_entrada.title("ventana secundaria")
        ventana_entrada.geometry("100x50")
        entrada=Entry(ventana_entrada)
        entrada.insert(0,"ingrsa actividad")
        entrada.grid(row=0)
        def boton_enviar():
            botonL1.config(text=entrada.get())
        boton_enviar=Button(ventana_entrada,text="guardar",command=boton_enviar,bg="red")
        boton_enviar.grid(row=1)
        #boton1.config(text=alo)    
    """
    botonL1.grid(row=1, column=0)
        
    botonL2 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=2, column=0)

    botonL3 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=3, column=0)

    botonL4 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=4, column=0)

    botonL5 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=5, column=0)

    botonL6 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=6, column=0)

    #Botones Martes

    botonM1 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=1, column=1)

    botonM2 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=2, column=1)

    botonM3 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=3, column=1)

    botonM4 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=4, column=1)

    botonM5 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=5, column=1)

    botonM6 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=6, column=1)


    # Botones Miercoles 
    botonW1 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=1, column=2)

    botonW2 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=2, column=2)

    botonW3 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=3, column=2)

    botonW4 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=4, column=2)

    botonW5 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=5, column=2)

    botonW6 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=6, column=2)

    # Botones Jueves

    botonJ1 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=1, column=3)

    botonJ2 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=2, column=3)

    botonJ3 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=3, column=3)

    botonJ4 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=4, column=3)

    botonJ5 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=5, column=3)

    botonJ6 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=6, column=3)

    # Botones Viernes

    botonV1 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=1, column=4)

    botonV2 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=2, column=4)

    botonV3 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=3, column=4)

    botonV4 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=4, column=4)

    botonV5 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=5, column=4)

    botonV6 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=6, column=4)

    # Botones Sabado

    botonS1 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=1, column=5)

    botonS2 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=2, column=5)

    botonS3 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=3, column=5)

    botonS4 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=4, column=5)

    botonS5 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=5, column=5)

    botonS6 = Button(ventana_nueva, text = "enviar", bg="yellow",padx=20, pady= 12).grid(row=6, column=5)

Button(root,text="enviar", command=cambia_ventana, bg="red").grid(row=1,column=0)
root.mainloop()
