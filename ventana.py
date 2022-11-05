from tkinter import *
root = Tk()

# Definición de la función que creará la ventana en la que será posible visualizar el horario.

#a =amplitud; w = ancho; h = alto
a = 1
w = 42
h = 75

def cambia_ventana():

#Esta segunda función creará la ventana dedicada a ingresar las actividades.
    def ventana_entra_act():
        ventana_entrada = Toplevel()
        ventana_entrada.title("ventana secundaria")
        ventana_entrada.geometry("350x450")
        entrada = Entry(ventana_entrada)
        entrada.config(width = 60)
        entrada_dia =  Entry(ventana_entrada)
        entrada_dia.config(width = 31)
        entrada.insert(0, "Horario de la actividad en este formato:(Día de la semana, bloque)")
        entrada_dia.insert(0, "Nombre de la actividad en cuestión")
        entrada_dia.grid(row = 1)
        entrada.grid(row = 0)
        nueva_entrada=str(entrada.get())
        def boton_enviar():
            lista_entrada = str(entrada.get()).split(" ")
            letras = ["L","M","W","J","V","S"]
            numeros = ["1","2","3","4","5","6"]
            verificador = 0
            switch = True
            while verificador < len(letras) and switch:
                switch = False
                if letras[verificador] not in lista_entrada:
                    showinfo(message = "Ingrese los horarios en un formato correcto", title = "Error")
                else:
                    i = i + 1
                    switch = True
            verificador = 0
            switch = True
            while verificador < len(numeros) and switch:
                switch = False
                if numeros[verificador] not in lista_entrada:
                    showinfo(message = "Ingrese los bloques en un formato correcto", title = "Error")
                else:
                    i = i + 1
                    switch = True
            for dia in letras:
                if dia == lista_entrada[0]:
                    j = int(letras.index(dia))
            for bloque in numeros:
                if bloque == lista_entrada[1]:
                    i = int(numeros.index(bloque))
            texto = Label(root, text = entrada_dia.get(), bg ="lightgreen", font = ("Arial", 12)).grid(row = i + 1, column = j + 1)
            
        boton_enviar=Button(ventana_entrada,text="guardar",command=boton_enviar,bg="red")
        boton_enviar.grid(row=2)


    # Asignacion de bloques, se vizualizarán en la columna de la izquierda e indicarán el bloque
    # horario correspondiente.
    root = Toplevel()
    root.title("Horario")
    root.geometry("300x450")
    
    bloque1 = Frame(root)
    textoB1 = Label(root, text = "Bloque 1", bg = "orange", font = ("Arial",6)).grid(row = 1, column = 0)
    bloque1.config(bg = "orange", width = a * w, height = a * h)
    bloque1.grid(row = 1, column = 0)

    bloque2 = Frame(root)
    textoB2 = Label(root, text = "Bloque 2", bg = "darkorange", font = ("Arial",6)).grid(row = 2, column = 0)
    bloque2.config(bg = "darkorange", width = a * w, height = a * h)
    bloque2.grid(row = 2, column =0)

    bloque3 = Frame(root)
    textoB3 = Label(root, text = "Bloque 3", bg = "orange", font = ("Arial",6)).grid(row = 3, column = 0)
    bloque3.config(bg = "orange", width = a * w, height = a * h)
    bloque3.grid(row = 3, column =0)

    bloque4 = Frame(root)
    textoB4 = Label(root, text = "Bloque 4", bg = "darkorange", font = ("Arial",6)).grid(row = 4, column = 0)
    bloque4.config(bg = "darkorange", width = a * w, height = a * h)
    bloque4.grid(row = 4, column =0)

    bloque5 = Frame(root)
    textoB5 = Label(root, text = "Bloque 5", bg = "orange", font = ("Arial",6)).grid(row = 5, column = 0)
    bloque5.config(bg = "orange", width = a * w, height = a * h)
    bloque5.grid(row = 5, column =0)

    bloque6 = Frame(root)
    textoB6 = Label(root, text = "Bloque 6", bg = "darkorange", font = ("Arial",6)).grid(row = 6, column = 0)
    bloque6.config(bg = "darkorange", width = a * w, height = a * h)
    bloque6.grid(row = 6, column =0)

    # Aquí abajo se mostrará cada bloque de cada día correspondiente, generando como un sistema
    # de coordenadas.

    #Lunes
    
    lunes1 = Frame(root)
    lunes1.config(bg = "lightgreen", width = a * w, height = a * h)
    lunes1.grid(row = 1, column = 1)

    lunes2 = Frame(root)
    lunes2.config(bg = "lightblue", width = a * w, height = a * h)
    lunes2.grid(row = 2, column = 1)

    lunes3 = Frame(root)
    lunes3.config(bg = "lightgreen",width = a * w, height = a * h)
    lunes3.grid(row = 3, column = 1)

    lunes4 = Frame(root)
    lunes4.config(bg = "lightblue", width = a * w, height = a * h)
    lunes4.grid(row = 4, column = 1)

    lunes5 = Frame(root)
    lunes5.config(bg = "lightgreen", width = a * w, height = a * h)
    lunes5.grid(row = 5, column = 1)

    lunes6 = Frame(root)
    lunes6.config(bg = "lightblue", width = a * w, height = a * h)
    lunes6.grid(row = 6, column = 1)


    #Martes
    martes1 = Frame(root)
    martes1.config(bg = "lightblue", width = a * w, height = a * h)
    martes1.grid(row = 1, column = 2)

    martes2 = Frame(root)
    martes2.config(bg = "lightgreen", width = a * w, height = a * h)
    martes2.grid(row = 2, column = 2)

    martes3 = Frame(root)
    martes3.config(bg = "lightblue", width = a * w, height = a * h)
    martes3.grid(row = 3, column = 2)

    martes4 = Frame(root)
    martes4.config(bg = "lightgreen", width = a * w, height = a * h)
    martes4.grid(row = 4, column = 2)

    martes5 = Frame(root)
    martes5.config(bg = "lightblue", width = a * w, height = a * h)
    martes5.grid(row = 5, column = 2)

    martes6 = Frame(root)
    martes6.config(bg = "lightgreen", width = a * w, height = a * h)
    martes6.grid(row = 6, column = 2)


    #Miércoles
    miercoles1 = Frame(root)
    miercoles1.config(bg = "lightgreen", width = a * w, height = a * h)
    miercoles1.grid(row = 1, column = 3)

    miercoles2 = Frame(root)
    miercoles2.config(bg = "lightblue", width = a * w, height = a * h)
    miercoles2.grid(row = 2, column = 3)

    miercoles3 = Frame(root)
    miercoles3.config(bg = "lightgreen", width = a * w, height = a * h)
    miercoles3.grid(row = 3, column = 3)

    miercoles4 = Frame(root)
    miercoles4.config(bg = "lightblue", width = a * w, height = a * h)
    miercoles4.grid(row = 4, column = 3)

    miercoles5 = Frame(root)
    miercoles5.config(bg = "lightgreen", width = a * w, height = a * h)
    miercoles5.grid(row = 5, column = 3)

    miercoles = Frame(root)
    miercoles.config(bg = "lightblue", width = a * w, height = a * h)
    miercoles.grid(row = 6, column = 3)


    #Jueves
    jueves1 = Frame(root)
    jueves1.config(bg = "lightblue", width = a * w, height = a * h)
    jueves1.grid(row = 1, column = 4)

    jueves2 = Frame(root)
    jueves2.config(bg = "lightgreen", width = a * w, height = a * h)
    jueves2.grid(row = 2, column = 4)

    jueves3 = Frame(root)
    jueves3.config(bg = "lightblue", width = a * w, height = a * h)
    jueves3.grid(row = 3, column = 4)

    jueves4 = Frame(root)
    jueves4.config(bg = "lightgreen", width = a * w, height = a * h)
    jueves4.grid(row = 4, column = 4)

    jueves5 = Frame(root)
    jueves5.config(bg = "lightblue", width = a * w, height = a * h)
    jueves5.grid(row = 5, column = 4)

    jueves6 = Frame(root)
    jueves6.config(bg = "lightgreen", width = a * w, height = a * h)
    jueves6.grid(row = 6, column = 4)



    #Viernes
    viernes1 = Frame(root)
    viernes1.config(bg = "lightgreen", width = a * w, height = a * h)
    viernes1.grid(row = 1, column = 5)

    viernes2 = Frame(root)
    viernes2.config(bg = "lightblue", width = a * w, height = a * h)
    viernes2.grid(row = 2, column = 5)

    viernes3 = Frame(root)
    viernes3.config(bg = "lightgreen", width = a * w, height = a * h)
    viernes3.grid(row = 3, column = 5)

    viernes4 = Frame(root)
    viernes4.config(bg = "lightblue", width = a * w, height = a * h)
    viernes4.grid(row = 4, column = 5)

    viernes5 = Frame(root)
    viernes5.config(bg = "lightgreen", width = a * w, height = a * h)
    viernes5.grid(row = 5, column = 5)

    viernes6 = Frame(root)
    viernes6.config(bg = "lightblue", width = a * w, height = a * h)
    viernes6.grid(row = 6, column = 5)



    #Sábado
    sabado1 = Frame(root)
    sabado1.config(bg = "lightblue", width = a * w, height = a * h)
    sabado1.grid(row = 1, column = 6)

    sabado2 = Frame(root)
    sabado2.config(bg = "lightgreen", width = a * w, height = a * h)
    sabado2.grid(row = 2, column = 6)

    sabado3 = Frame(root)
    sabado3.config(bg = "lightblue", width = a * w, height = a * h)
    sabado3.grid(row = 3, column = 6)

    sabado4 = Frame(root)
    sabado4.config(bg = "lightgreen", width = a * w, height = a * h)
    sabado4.grid(row = 4, column = 6)

    sabado5 = Frame(root)
    sabado5.config(bg = "lightblue", width = a * w, height = a * h)
    sabado5.grid(row = 5, column = 6)

    sabado6 = Frame(root)
    sabado6.config(bg = "lightgreen", width = a * w, height = a * h)
    sabado6.grid(row = 6, column = 6)

    #Asignación de días, se mostrará el nombre del día a lo largo de la primera fila


    lunes = Frame(root)
    textoL = Label(root, text = "Lunes", bg = "orange", font = ("Arial",6)).grid(row = 0, column = 1)
    lunes.config(bg = "orange", width = 42, height =  30)
    lunes.grid(row = 0, column = 1)

    martes = Frame(root)
    textoM = Label(root, text = "Martes", bg = "darkorange", font = ("Arial",6)).grid(row = 0, column = 2)
    martes.config(bg = "darkorange", width = 42, height =  30)
    martes.grid(row = 0, column =2)

    miercoles = Frame(root)
    textoW = Label(root, text = "Miércoles", bg = "orange", font = ("Arial",6)).grid(row = 0, column = 3)
    miercoles.config(bg = "orange", width = 42, height =  30)
    miercoles.grid(row = 0, column =3)

    jueves = Frame(root)
    textoJ = Label(root, text = "Jueves", bg = "darkorange", font = ("Arial",6)).grid(row = 0, column = 4)
    jueves.config(bg = "darkorange", width = 42, height =  30)
    jueves.grid(row = 0, column =4)

    viernes = Frame(root)
    textoV = Label(root, text = "Viernes", bg = "orange", font = ("Arial",6)).grid(row = 0, column = 5)
    viernes.config(bg = "orange", width = 42, height =  30)
    viernes.grid(row = 0, column =5)

    sabado = Frame(root)
    textoV = Label(root, text = "Sábado", bg = "darkorange", font = ("Arial",6)).grid(row = 0, column = 6)
    sabado.config(bg = "darkorange", width = 42, height =  30)
    sabado.grid(row = 0, column =6)

    # Definición del botón, al hacer click, este llevará a la ventana para ingresar actividad


    boton = Button(root, text = "+", bg= "cyan", font = ("Arial",8), padx=14, pady= 3, command = ventana_entra_act).grid(row=0, column=0)

# Ventana inicial, incluye una pequeña explicación de lo que hace el programa y un botón que lleva a la ventana del horario


marco_principal1 = Frame()
texto = Label(root,
              text= "Este programa tiene la finalidad\nde ayudarte a organizar tu horario, para así\nmejorar tu rendimiento académico\n y lograr optimizar tu tiempo",
              bg = "pink")


marco_principal1.grid(row=0, column=0)
texto.grid(row=0, column=0)

marco_principal1.config(width = "260", height = "370")
marco_principal1.config(bg = "pink")

boton_inicio = Button(root,text="enviar", command=cambia_ventana, bg="red").grid(row=1,column=0)
root.mainloop()
