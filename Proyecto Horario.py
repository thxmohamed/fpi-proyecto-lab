# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 0-L-19
# PROFESOR DE TEORÍA: ALEJANDRO CISTERNA VILLALOBOS
# PROFESOR DE LABORATORIO: Gery Gerena
# GRUPO : 3
#
# AUTORES
# INTEGRANTES: -Mohamed Al-Marzuk/rut:22.594.262-5 
#               -Victor Duarte/rut:
#               -Vicente Fernandez/rut:20.957.898-0 
#               -Rodrigo Sepulveda/rut:20.651.185-0
#               -Nicolas Morales/rut:21.566.658-1.
# CARRERA: Ingeniería Civil Informática e Ingenieria Civil Electrica

# Este programa mostrará un horario separado por bloques de la universidad, donde el usuario podrá
# ingresar sus actividades diarias y mirarlas por pantalla, ayudando a la
# organización de su tiempo. Para esto, se utilizará la librería Tkinter. 

# BLOQUE DE DEFINICIÓN

# IMPORTACIÓN DE FUNCIONES

from tkinter import *
from tkinter.messagebox import *
root = Tk()

# DEFINICIÓN DE FUNCIONES

# Definición de la función que creará la ventana en la que será posible visualizar el horario.

def cambia_ventana():
    root.withdraw()
#Esta segunda función creará la ventana dedicada a ingresar las actividades.
    def ventana_entra_act():
        ventana_entrada=Toplevel()
        ventana_entrada.title("Agregar Actividad")
        ventana_entrada.geometry("300x450")
        # entrada es la variable que define el cuadro de texto en donde se ingresará el bloque

        entrada=Entry(ventana_entrada, bg = "aquamarine", fg = "black", width =49)

        marco1 = Frame(ventana_entrada)
        marco1.config(bg = "lightgreen", width = 300, height = 100)
        marco1.grid(row = 0, column = 0)

        marco2 = Frame(ventana_entrada)
        marco2.config(bg = "lightgreen", width = 300, height = 50)
        marco2.grid(row = 2, column = 0)

        marco3 = Frame(ventana_entrada)
        marco3.config(bg = "lightgreen", width = 300, height = 130)
        marco3.grid(row = 3, column = 0)

        marco4 = Frame(ventana_entrada)
        marco4.config(bg = "lightgreen", width = 300, height = 150)
        marco4.grid(row = 5, column = 0)
        # La variable llamada bloque se trata de una explicación al usuario de lo 
        # que tiene que ingresar en el cuadro de texto y en qué formato hacerlo
        
        bloque = Label(ventana_entrada, text = "Ingrese el Bloque separado por un espacio. Ej: (L 5)", bg = "lightgreen", font = ("Arial", 9)).grid(row = 0, column = 0)
        entrada.grid(row=1)
        nueva_entrada=str(entrada.get())
        # una explicación de lo que tiene que ingresar el usuario en el segundo cuadro de texto
        explicacion = Label(ventana_entrada, text = "Ingrese su actividad, tras esto,\n"
                            "pulse en asignar", bg = "lightgreen", font = ("Arial", 9)).grid(row = 3, column = 0)

        actividad = Entry(ventana_entrada, bg = "aquamarine", fg = "black", width = 49)
        actividad.grid(row=4)

        # Aquí se define el botón de "asignar", al pulsar este botón, la actividad ingresada se
        # ubicará en el bloque ingresado

        def boton_enviar():
            lista_entrada = str(entrada.get()).split(" ")       
            letras = ["L","M","W","J","V","S"]
            numeros = ["1","2","3","4","5","6"]
            verificador = 0
            switch = True
            while verificador < len(lista_entrada) and switch:
                switch = False
                if lista_entrada[verificador] in letras or \
                   lista_entrada[verificador] in numeros:
                    verificador = verificador + 1
                    switch = True
                else:
                    showinfo(message = "Ingrese los horarios en un formato correcto", title = "Error")
            for dia in letras:
                if dia == lista_entrada[0]:
                    j = letras.index(dia)
            for bloque in numeros:
                if bloque == lista_entrada[1]:
                    i = numeros.index(bloque)

            if (i +1) % 2 == 1 and (j + 1) % 2 == 1:                
                texto = Label(root2, text = actividad.get(), bg = "lightgreen", font = ("Arial", 8)).grid(row = i + 1, column = j + 1)
            elif (i + 1) % 2 == 0 and (j + 1) % 2 == 0:
                texto = Label(root2, text = actividad.get(), bg = "lightgreen", font = ("Arial", 8)).grid(row = i + 1, column = j + 1)        
            else:
                texto = Label(root2, text = actividad.get(), bg = "lightblue", font = ("Arial", 8)).grid(row = i + 1, column = j + 1)
            
        boton_enviar=Button(ventana_entrada,text="Asignar",command=boton_enviar,bg="green", font = ("Arial", 12))
        boton_enviar.grid(row=2)

        boton_cerrar = Button(ventana_entrada, text = "Finalizar Programa", command = root.destroy, bg = "red",
                              fg = "white", font = ("Arial", 12)).grid(row = 5)

    # Asignacion de bloques, se visualizarán en la columna de la izquierda e indicarán el bloque
    # horario correspondiente.
    root2 =Toplevel()
    root2.title("Horario")
    root2.geometry("700x630")

    
    bloque1 = Frame(root2)
    textoB1 = Label(root2, text = "Bloque 1", bg = "orange", font = ("Arial",14)).grid(row = 1, column = 0)
    bloque1.config(bg = "orange", width = 100, height =  100)
    bloque1.grid(row = 1, column = 0)

    bloque2 = Frame(root2)
    textoB2 = Label(root2, text = "Bloque 2", bg = "darkorange", font = ("Arial",14)).grid(row = 2, column = 0)
    bloque2.config(bg = "darkorange", width = 100, height = 100)
    bloque2.grid(row = 2, column =0)

    bloque3 = Frame(root2)
    textoB3 = Label(root2, text = "Bloque 3", bg = "orange", font = ("Arial",14)).grid(row = 3, column = 0)
    bloque3.config(bg = "orange", width = 100, height = 100)
    bloque3.grid(row = 3, column =0)

    bloque4 = Frame(root2)
    textoB4 = Label(root2, text = "Bloque 4", bg = "darkorange", font = ("Arial",14)).grid(row = 4, column = 0)
    bloque4.config(bg = "darkorange", width = 100, height = 100)
    bloque4.grid(row = 4, column =0)

    bloque5 = Frame(root2)
    textoB5 = Label(root2, text = "Bloque 5", bg = "orange", font = ("Arial",14)).grid(row = 5, column = 0)
    bloque5.config(bg = "orange", width = 100, height = 100)
    bloque5.grid(row = 5, column =0)

    bloque6 = Frame(root2)
    textoB6 = Label(root2, text = "Bloque 6", bg = "darkorange", font = ("Arial",14)).grid(row = 6, column = 0)
    bloque6.config(bg = "darkorange", width = 100, height = 100)
    bloque6.grid(row = 6, column =0)

    # Aquí abajo se mostrará cada bloque de cada día correspondiente, generando como un sistema
    # de coordenadas.

    #Lunes
    
    lunes1 = Frame(root2)
    lunes1.config(bg = "lightgreen", width = 100, height = 100)
    lunes1.grid(row = 1, column = 1)

    lunes2 = Frame(root2)
    lunes2.config(bg = "lightblue", width = 100, height = 100)
    lunes2.grid(row = 2, column = 1)

    lunes3 = Frame(root2)
    lunes3.config(bg = "lightgreen", width = 100, height = 100)
    lunes3.grid(row = 3, column = 1)

    lunes4 = Frame(root2)
    lunes4.config(bg = "lightblue", width = 100, height = 100)
    lunes4.grid(row = 4, column = 1)

    lunes5 = Frame(root2)
    lunes5.config(bg = "lightgreen", width = 100, height = 100)
    lunes5.grid(row = 5, column = 1)

    lunes6 = Frame(root2)
    lunes6.config(bg = "lightblue", width = 100, height = 100)
    lunes6.grid(row = 6, column = 1)


    #Martes
    martes1 = Frame(root2)
    martes1.config(bg = "lightblue", width = 100, height = 100)
    martes1.grid(row = 1, column = 2)

    martes2 = Frame(root2)
    martes2.config(bg = "lightgreen", width = 100, height = 100)
    martes2.grid(row = 2, column = 2)

    martes3 = Frame(root2)
    martes3.config(bg = "lightblue", width = 100, height = 100)
    martes3.grid(row = 3, column = 2)

    martes4 = Frame(root2)
    martes4.config(bg = "lightgreen", width = 100, height = 100)
    martes4.grid(row = 4, column = 2)

    martes5 = Frame(root2)
    martes5.config(bg = "lightblue", width = 100, height = 100)
    martes5.grid(row = 5, column = 2)

    martes6 = Frame(root2)
    martes6.config(bg = "lightgreen", width = 100, height = 100)
    martes6.grid(row = 6, column = 2)


    #Miércoles
    miercoles1 = Frame(root2)
    miercoles1.config(bg = "lightgreen", width = 100, height = 100)
    miercoles1.grid(row = 1, column = 3)

    miercoles2 = Frame(root2)
    miercoles2.config(bg = "lightblue", width = 100, height = 100)
    miercoles2.grid(row = 2, column = 3)

    miercoles3 = Frame(root2)
    miercoles3.config(bg = "lightgreen", width = 100, height = 100)
    miercoles3.grid(row = 3, column = 3)

    miercoles4 = Frame(root2)
    miercoles4.config(bg = "lightblue", width = 100, height = 100)
    miercoles4.grid(row = 4, column = 3)

    miercoles5 = Frame(root2)
    miercoles5.config(bg = "lightgreen", width = 100, height = 100)
    miercoles5.grid(row = 5, column = 3)

    miercoles = Frame(root2)
    miercoles.config(bg = "lightblue", width = 100, height = 100)
    miercoles.grid(row = 6, column = 3)


    #Jueves
    jueves1 = Frame(root2)
    jueves1.config(bg = "lightblue", width = 100, height = 100)
    jueves1.grid(row = 1, column = 4)

    jueves2 = Frame(root2)
    jueves2.config(bg = "lightgreen", width = 100, height = 100)
    jueves2.grid(row = 2, column = 4)

    jueves3 = Frame(root2)
    jueves3.config(bg = "lightblue", width = 100, height = 100)
    jueves3.grid(row = 3, column = 4)

    jueves4 = Frame(root2)
    jueves4.config(bg = "lightgreen", width = 100, height = 100)
    jueves4.grid(row = 4, column = 4)

    jueves5 = Frame(root2)
    jueves5.config(bg = "lightblue", width = 100, height = 100)
    jueves5.grid(row = 5, column = 4)

    jueves6 = Frame(root2)
    jueves6.config(bg = "lightgreen", width = 100, height = 100)
    jueves6.grid(row = 6, column = 4)



    #Viernes
    viernes1 = Frame(root2)
    viernes1.config(bg = "lightgreen", width = 100, height = 100)
    viernes1.grid(row = 1, column = 5)

    viernes2 = Frame(root2)
    viernes2.config(bg = "lightblue", width = 100, height = 100)
    viernes2.grid(row = 2, column = 5)

    viernes3 = Frame(root2)
    viernes3.config(bg = "lightgreen", width = 100, height = 100)
    viernes3.grid(row = 3, column = 5)

    viernes4 = Frame(root2)
    viernes4.config(bg = "lightblue", width = 100, height = 100)
    viernes4.grid(row = 4, column = 5)

    viernes5 = Frame(root2)
    viernes5.config(bg = "lightgreen", width = 100, height = 100)
    viernes5.grid(row = 5, column = 5)

    viernes6 = Frame(root2)
    viernes6.config(bg = "lightblue", width = 100, height = 100)
    viernes6.grid(row = 6, column = 5)



    #Sábado
    sabado1 = Frame(root2)
    sabado1.config(bg = "lightblue", width = 100, height = 100)
    sabado1.grid(row = 1, column = 6)

    sabado2 = Frame(root2)
    sabado2.config(bg = "lightgreen", width = 100, height = 100)
    sabado2.grid(row = 2, column = 6)

    sabado3 = Frame(root2)
    sabado3.config(bg = "lightblue", width = 100, height = 100)
    sabado3.grid(row = 3, column = 6)

    sabado4 = Frame(root2)
    sabado4.config(bg = "lightgreen", width = 100, height = 100)
    sabado4.grid(row = 4, column = 6)

    sabado5 = Frame(root2)
    sabado5.config(bg = "lightblue", width = 100, height = 100)
    sabado5.grid(row = 5, column = 6)

    sabado6 = Frame(root2)
    sabado6.config(bg = "lightgreen", width = 100, height = 100)
    sabado6.grid(row = 6, column = 6)

    #Asignación de días, se mostrará el nombre del día a lo largo de la primera fila


    lunes = Frame(root2)
    textoL = Label(root2, text = "Lunes", bg = "orange", font = ("Arial",14)).grid(row = 0, column = 1)
    lunes.config(bg = "orange", width = 100, height =  30)
    lunes.grid(row = 0, column = 1)

    martes = Frame(root2)
    textoM = Label(root2, text = "Martes", bg = "darkorange", font = ("Arial",14)).grid(row = 0, column = 2)
    martes.config(bg = "darkorange", width = 100, height = 30)
    martes.grid(row = 0, column =2)

    miercoles = Frame(root2)
    textoW = Label(root2, text = "Miércoles", bg = "orange", font = ("Arial",14)).grid(row = 0, column = 3)
    miercoles.config(bg = "orange", width = 100, height = 30)
    miercoles.grid(row = 0, column =3)

    jueves = Frame(root2)
    textoJ = Label(root2, text = "Jueves", bg = "darkorange", font = ("Arial",14)).grid(row = 0, column = 4)
    jueves.config(bg = "darkorange", width = 100, height = 30)
    jueves.grid(row = 0, column =4)

    viernes = Frame(root2)
    textoV = Label(root2, text = "Viernes", bg = "orange", font = ("Arial",14)).grid(row = 0, column = 5)
    viernes.config(bg = "orange", width = 100, height = 30)
    viernes.grid(row = 0, column =5)

    sabado = Frame(root2)
    textoV = Label(root2, text = "Sábado", bg = "darkorange", font = ("Arial",14)).grid(row = 0, column = 6)
    sabado.config(bg = "darkorange", width = 100, height = 30)
    sabado.grid(row = 0, column =6)

    # Definición del botón, al hacer click, este llevará a la ventana para ingresar actividad


    boton = Button(root2, text = "Agregar", bg= "cyan", font = ("Arial",11), padx=17.5, pady= 2.1, command = ventana_entra_act).grid(row=0, column = 0)
    
# DEFINICIÓN DE CONSTANTES
# De momento, en nuestro programa no se definió ninguna constante


# BLOQUE PRINCIPAL
 
# ENTRADA

# La entrada está considerada dentro de la función ventana_entra_act(), definida más arriba
    
# Ventana inicial, incluye una pequeña explicación de lo que hace el programa y un botón que lleva a la ventana del horario

marco_principal1 = Frame()
texto = Label(root,
              text= "Este programa tiene la finalidad\nde ayudarte a organizar tu horario, para así\n"
              "mejorar tu rendimiento académico\n y lograr optimizar tu tiempo,\npara esto debes pulsar el botón de abajo,\n"
              "y cuando se abra la nueva ventana\ndebes pulsar el botón de la esquina\nsuperior izquierda",
              bg = "pink")

# PROCESAMIENTO

marco_principal1.grid(row=0, column=0)
texto.grid(row=0, column=0)

marco_principal1.config(width = "260", height = "370")
marco_principal1.config(bg = "pink")

boton_inicio = Button(root,text="Comenzar", command=cambia_ventana, bg="red", width="28", font = ("Arial", 12), fg = "white").grid(row=1,column=0)

# SALIDA

root.mainloop()
