# FUNDAMENTOS DE PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 0-L-19
# PROFESOR DE TEORÍA: ALEJANDRO CISTERNA VILLALOBOS
# PROFESOR DE LABORATORIO: Gery Gerena
# GRUPO : 3
# AUTORES
# INTEGRANTES: -Mohamed Al-Marzuk/rut: 22.594.262-5 
#               -Victor Duarte/rut: 21.467.246-4
#               -Vicente Fernandez/rut: 20.957.898-0 
#               -Nicolas Morales/rut: 21.566.658-1.
# CARRERA: Ingeniería Civil Informática e Ingenieria Civil Electrica

# Este programa mostrará un horario separado por bloques de la universidad, donde el usuario podrá
# ingresar sus actividades diarias y mirarlas por pantalla, ayudando a la
# organización de su tiempo. Para esto, se utilizará la librería Tkinter. 

# BLOQUE DE DEFINICIÓN

# IMPORTACIÓN DE FUNCIONES

from tkinter import *
from tkinter.messagebox import *
from datetime import datetime
from datetime import timedelta
import threading
import time
# DEFINICIÓN DE FUNCIONES
# Definiremos la función que leerá el horario
# Definición de la función que creará la ventana en la que será posible visualizar el horario.
def cambia_ventana():
    root.withdraw()

# Estas son listas de 7 strings que se definen para tener un lugar en donde
# guardar los datos ingresados por el usuario, la primera columna representa
# los bloques del día predefinidos por nosotros, y las siguientes 6 posiciones son
# las actividades de cada día en el bloque correspondiente, siendo la posición 1 de
# cada lista el lunes, la pos 2 el martes, y así hasta la pos 6 que es el sábado.
    lista_bloque1=["Bloque 1","","","","","","","",""]
    lista_bloque2=["Bloque 2","","","","","","","",""]
    lista_bloque3=["Bloque 3","","","","","","","",""]
    lista_bloque4=["Bloque 4","","","","","","","",""]
    lista_bloque5=["Bloque 5","","","","","","","",""]
    lista_bloque6=["Bloque 6","","","","","","","",""]
        
    lista_bloques= ["",lista_bloque1,lista_bloque2,lista_bloque3,
                    lista_bloque4,lista_bloque5,lista_bloque6]

#Aquí se define la función para el recordatorio
    def recordatorio():
        def recordatorio1(run):
            # Este ciclo está hecho para que se repita siempre
            # sin embargo, no hará que se pegue el programa, pues
            # se ejecuta en segundo plano.
            while run.is_set():
                #Esta variable de aquí lo que hace es guardar la hora actual del sistema
                t_actual= datetime.now()
                #Estas son constantes que se utilizarán para calcular el tiempo restante
                #para la siguiente actividad ingresada
                T_BLOQUE1 = datetime(t_actual.year,t_actual.month,t_actual.day,8,15,0000)
                T_BLOQUE2 = datetime(t_actual.year,t_actual.month,t_actual.day,9,50,00,0000)
                T_BLOQUE3 = datetime(t_actual.year,t_actual.month,t_actual.day,11,25,00,0000)
                T_BLOQUE4 = datetime(t_actual.year,t_actual.month,t_actual.day,13,45,00,0000)
                T_BLOQUE5 = datetime(t_actual.year,t_actual.month,t_actual.day,15,20,00,0000)
                T_BLOQUE6 = datetime(t_actual.year,t_actual.month,t_actual.day,16,55,00,0000)
                T_FIN_DIA = datetime(t_actual.year,t_actual.month,t_actual.day,23,59,59,0000)
                T_DIA_SGTE = datetime(t_actual.year,t_actual.month,t_actual.day,00,00,00,0000)
                T_BLOQUES = ["",T_BLOQUE1,T_BLOQUE2,T_BLOQUE3,T_BLOQUE4,
                             T_BLOQUE5,T_BLOQUE6,T_FIN_DIA,T_DIA_SGTE]
                actividad_arec = "No hay actividades para hoy"
                #El objetivo es calcular la actividad a recordar
                #Calculamos el bloque en el que estamos actualmente con un ciclo
                bloque_siguiente = 1
                while bloque_siguiente < len(lista_bloques) + 1 and t_actual > T_BLOQUES[bloque_siguiente]:
                    bloque_siguiente += 1
                #Calculamos el día en el que estamos con formato 1 = lunes y 6 = sábado, 0 = domingo
                dia = t_actual.strftime("%w")
                dia = int(dia)
                #Si estamos después del bloque 6; bloque_siguiente = 7
                if bloque_siguiente == 7:
                    dia += 1
                    bloque_siguiente = 1
                if dia == 0 or dia == 7:
                    dia = "domingo"
                # Ahora que tenemos el bloque y el día en el que estamos tenemos la actividad a recordar
                #Esto cubrirá el caso en el que el día de hoy sea domingo
                if dia == "domingo":
                    dia = 1
                    actividad_arec = lista_bloques[bloque_siguiente][dia]
                #Este ciclo cubrirá el caso en el que el alumno tenga alguna ventana en su horario
                #Recorrerá el calendario hasta encontrar alguna actividad que no sea: ""
                #Para que no se quede trabada, hay que verificar que el horario no esté vacío
                if lista_bloque1 == ["Bloque 1","","","","","","","",""] and \
                    lista_bloque2 ==["Bloque 2","","","","","","","",""] and \
                    lista_bloque3 == ["Bloque 3","","","","","","","",""] and \
                    lista_bloque4 == ["Bloque 4","","","","","","","",""] and \
                    lista_bloque5 == ["Bloque 5","","","","","","","",""] and \
                    lista_bloque6 == ["Bloque 6","","","","","","","",""]:
                    showinfo(message= "No tiene ninguna actividad en su horario...",
                             title="RECORDATORIO")
                else:
                    while actividad_arec == "":
                        bloque_siguiente += 1
                        if bloque_siguiente != 7:
                            actividad_arec = lista_bloques[bloque_siguiente][dia]
                        else:
                            bloque_siguiente = 1
                            dia += 1
                            if dia != 7:
                                actividad_arec = lista_bloques[bloque_siguiente][dia]
                            else:
                                dia = 1
                                actividad_arec = lista_bloques[bloque_siguiente][dia]
                    #Ahora que tenemos las coordenadas de la actividad, calculamos el tiempo restante
                    if dia >= int(t_actual.strftime("%w")) and t_actual < T_BLOQUE6:
                        delta = dia - int(t_actual.strftime("%w"))
                    else:
                        delta = dia - int(t_actual.strftime("%w")) + 7
                    bloque_arec = T_BLOQUES[bloque_siguiente] 
                    bloque_arec += timedelta(days = delta)
                    t_restante = bloque_arec - t_actual

                    if "days" in str(t_restante):
                        t_restante = str(t_restante).replace("days", "días")
                    elif "day" in str(t_restante):
                        t_restante = str(t_restante).replace("day", "día")
                    #Ahora soltamos la notificación
                    showinfo(message= "Le queda " + str(t_restante) + " horas" + " para " + str(actividad_arec),
                             title="RECORDATORIO")
        #Finalmente, esta parte es para que se ejecute en segundo plano.
                time.sleep(600)
        run = threading.Event()
        run.set()
        t = threading.Thread(target = recordatorio1, args = (run,)) # Se ejecuta en segundo plano
        t.start()
        #El siguiente botón será para detener los recordatorios
        def detener():
            run.clear()
            showinfo(message= "Se han detenido los recordatorios", title="STOP")
        boton_detener = Button(root2, text = "Detener", bg= "red", font = ("Arial",11), padx= 18,\
                   pady= 2.1, command = detener, fg = "white").grid(row=7, column = 2)
    #Esta segunda función creará la ventana dedicada a ingresar las actividades.
    def ventana_entra_act():
        ventana_entrada = Toplevel()
        ventana_entrada.title("Agregar Actividad")
        ventana_entrada.geometry("300x500")
        # entrada es la variable que define el cuadro de texto en donde se ingresará el bloque

        entrada=Entry(ventana_entrada, bg = "aquamarine", fg = "black", width =49)

        marco1 = Frame(ventana_entrada)
        marco1.config(bg = "lightgreen", width = 300, height = 70)
        marco1.grid(row = 0, column = 0)

        marco2 = Frame(ventana_entrada)
        marco2.config(bg = "lightgreen", width = 300, height = 50)
        marco2.grid(row = 2, column = 0)

        marco3 = Frame(ventana_entrada)
        marco3.config(bg = "lightgreen", width = 300, height = 70)
        marco3.grid(row = 3, column = 0)

        marco4 = Frame(ventana_entrada)
        marco4.config(bg = "lightgreen", width = 300, height = 50)
        marco4.grid(row = 5, column = 0)

        marco5 = Frame(ventana_entrada)
        marco5.config(bg = "lightgreen", width = 300, height = 60)
        marco5.grid(row = 6, column = 0)
        
        marco6 = Frame(ventana_entrada)
        marco6.config(bg = "lightgreen", width = 300, height = 55)
        marco6.grid(row = 7, column = 0)

        marco6 = Frame(ventana_entrada)
        marco6.config(bg = "lightgreen", width = 300, height = 55)
        marco6.grid(row = 8, column = 0)

        marco6 = Frame(ventana_entrada)
        marco6.config(bg = "lightgreen", width = 300, height = 55)
        marco6.grid(row = 9, column = 0)
        
        # La variable llamada bloque se trata de una explicación al usuario de lo 
        # que tiene que ingresar en el cuadro de texto y en qué formato hacerlo
        
        bloque = Label(ventana_entrada, text = "Ingrese el Bloque. Ej: (L5)",\
                       bg = "lightgreen", font = ("Arial", 9)).grid(row = 0, column = 0)
        entrada.grid(row=1)
        # una explicación de lo que tiene que ingresar el usuario en el segundo cuadro de texto
        explicacion = Label(ventana_entrada, text = "Ingrese su actividad, tras esto,\n"\
                            "pulse en asignar", bg = "lightgreen",
                            font = ("Arial", 9)).grid(row = 3, column = 0)

        actividad = Entry(ventana_entrada, bg = "aquamarine", fg = "black", width = 49)
        actividad.grid(row=4)

        # otra explicación para que el usuario ingrese el nombre del archivo csv que va
        # a usar para su horario
        explicacion_archivo = Label(ventana_entrada, text = "Ingrese el nombre del archivo csv \n"\
                            "que va a usar para abrir su horario (sin formato)", bg = "lightgreen",\
                            font = ("Arial", 9)).grid(row = 5, column = 0)
        entrada_archivo = Entry(ventana_entrada, bg = "aquamarine", fg = "black", width = 49)
        entrada_archivo.grid(row=6)
        
        # Aquí se define el botón de "asignar", al pulsar este botón, la actividad ingresada se
        # ubicará en el bloque ingresado
        def boton_subir():
            with open(entrada_archivo.get() + ".csv","r") as calendario:
            # Hacemos una listas de listas que extraigan los datos del archivo
                lista = []
                for fila in calendario:
                    lista.append(fila.strip().split(";"))
            # Hacemos un ciclo que borre el ultimo elemento de cada sublista
            i = 1
            while i < len(lista):                
                lista[i].pop(-1)
                i += 1
            # Este ciclo lo que hace es leer el archivo y hacer que se vea en la interfaz
            # del programa
            i = 1
            while i < len(lista):
                j = 1
                while j < len(lista[1]):
                    # aquí reasignamos los elementos de las listas definidas anteriormente, para
                    # que no se pierda la información al guardarla de vuelta.
                    lista_bloque1[j] = lista[1][j]
                    lista_bloque2[j] = lista[2][j]
                    lista_bloque3[j] = lista[3][j]
                    lista_bloque4[j] = lista[4][j]
                    lista_bloque5[j] = lista[5][j]
                    lista_bloque6[j] = lista[6][j]
            
            # Esta de abajo es una comprobación meramente estética, para que los
            # colores del fondo coincidan con los colores del texto, mientras que el ciclo
            # lo que hace es ir agregando posición a posición la actividad del archivo
            # correspondiente.
                    if len(lista[i][j]) > 15:
                        if len(lista[i][j]) > 30:
                            actividad_a_poner = lista[i][j][0:15] + "\n" + lista[i][j][15:30] \
                                              + "\n" + lista[i][j][30:]
                            if (i + j) % 2 == 0:
                                texto = Label(root2, text = actividad_a_poner, bg = "lightgreen",\
                                              font = ("Arial", 8)).grid(row = i, column = j)    
                            else:
                                texto = Label(root2, text = actividad_a_poner, bg = "lightblue",\
                                              font = ("Arial", 8)).grid(row = i, column = j)
                                
                        else:
                            actividad_a_poner = lista[i][j][0:15] + "\n" + lista[i][j][15:]
                            if (i + j) % 2 == 0:
                                texto = Label(root2, text = actividad_a_poner, bg = "lightgreen",\
                                              font = ("Arial", 8)).grid(row = i, column = j)    
                            else:
                                texto = Label(root2, text = actividad_a_poner, bg = "lightblue",\
                                              font = ("Arial", 8)).grid(row = i, column = j)
                    else:
                        if (i + j) % 2 == 0:
                            texto = Label(root2, text = lista[i][j], bg = "lightgreen",\
                                            font = ("Arial", 8)).grid(row = i, column = j)      
                        else:
                            texto = Label(root2, text = lista[i][j], bg = "lightblue",\
                                            font = ("Arial", 8)).grid(row = i, column = j)
                    j = j + 1
                i = i + 1
            lista_bloques= [lista_bloque1,lista_bloque2,lista_bloque3,lista_bloque4,lista_bloque5,lista_bloque6]
        # El botón que sirve para subir un archivo al programa, utilizará la función de arriba
        boton_subir=Button(ventana_entrada,text = "Subir Archivo",\
                           command=boton_subir,bg = "green", font = ("Arial", 12))        
        boton_subir.grid(row = 7)
        
        def boton_asignar():
            # Aquí definimos una constante, que es una lista de 7 elementos, siendo el
            # primero (pos 0) un string vacío, y los siguientes los días de la semana, esto
            # con el fin de guardarlo en un archivo.
            #se guarda el dia y bloque seleciconado por el usuario como string 
            #y se convierte en mayusculas para evitar errores
            LISTA_DIAS = ["","Lunes", "Martes", "Miércoles","Jueves", "Viernes", "Sábado"]
            str_entrada = (entrada.get()).upper()     
            letras = ["L","M","W","J","V","S"]
            numeros = ["1","2","3","4","5","6"]

            #El siguiente if verificará si el bloque ingresado por el usuario sigue
            #el formato pedido, de no hacerlo, mostrará un mensaje de error.
            if str_entrada[0] not in letras or str_entrada[1] not in numeros:
                    showinfo(message = "Ingrese los horarios en un formato correcto", title = "Error")                

            # Este ciclo for lo que hace es agregar la actividad ingresada
            # por el usuario al bloque que corresponda.
            for dia in letras:
                if dia == str_entrada[0]:
                    i = letras.index(dia) + 1
            for bloque in numeros:
                if bloque == str_entrada[1]:
                    j = numeros.index(bloque) + 1
            # Este ciclo lo que hace es almacenar las actividades ingresadas
            # en la lista correspondiente de las 6 que fueron definidas
            # con anterioridad
            
            if j==1:
               lista_bloque1[i]=actividad.get()
            elif j==2:
                lista_bloque2[i]=actividad.get()
            elif j==3:
                lista_bloque3[i]=actividad.get()
            elif j==4:
                lista_bloque4[i]=actividad.get()
            elif j==5:
                lista_bloque5[i]=actividad.get()
            elif j==6:
                lista_bloque6[i]=actividad.get()

            lista_= [lista_bloque1,lista_bloque2,lista_bloque3,lista_bloque4,lista_bloque5,lista_bloque6]
        # Esta de aquí es la función para el botón guardar
            def boton_guardar():

                # Se hace un ciclo por cada una de las 7 listas definidas anteriormente
                # con el fin de agrupar todo en un único string separado por ";"
                i = 0
                dias_csv = ""
                while i < len(LISTA_DIAS):
                    dias_csv = dias_csv + LISTA_DIAS[i] + ";"
                    i += 1
                
                i = 0
                bloque1_csv = ""
                while i< len(lista_bloque1):
                    bloque1_csv = bloque1_csv + lista_bloque1[i] + ";"
                    i += 1

                i = 0
                bloque2_csv = ""
                while i< len(lista_bloque2):
                    bloque2_csv = bloque2_csv + lista_bloque2[i] + ";"
                    i += 1

                i = 0
                bloque3_csv = ""
                while i< len(lista_bloque3):
                    bloque3_csv = bloque3_csv + lista_bloque3[i] + ";"
                    i += 1

                i = 0
                bloque4_csv = ""
                while i< len(lista_bloque4):
                    bloque4_csv = bloque4_csv + lista_bloque4[i] + ";"
                    i += 1
                    
                i = 0
                bloque5_csv = ""
                while i< len(lista_bloque5):
                    bloque5_csv = bloque5_csv + lista_bloque5[i] + ";"
                    i += 1
                    
                i = 0
                bloque6_csv = ""
                while i< len(lista_bloque6):
                    bloque6_csv = bloque6_csv + lista_bloque6[i] + ";"
                    i += 1

                # Aquí simplemente se abre el archivo que ingresa el usuario, y se hace
                # la comprobación de en qué fila y en qué columna se encuentra, dependiendo
                # del bloque ingresado (M 4, W 6, etc).
                
                with open(entrada_archivo.get() + ".csv","w") as calendario:
                    str_entrada = (entrada.get()).upper()
                    letras = ["L","M","W","J","V","S"]
                    numeros = ["1","2","3","4","5","6"]

                # Este es el string que va a ser guardado en el archivo .csv, separado por saltos
                #de linea "\n"
                    horario_a_guardar = dias_csv + "\n" + bloque1_csv + "\n" + bloque2_csv + "\n" \
                                        +  bloque3_csv + "\n" + bloque4_csv + "\n" + bloque5_csv + "\n"  + bloque6_csv
                    calendario.write(horario_a_guardar)
            explicacion_guardar = Label(ventana_entrada, text = "Ingrese el nombre del archivo csv \n"\
                                "que va a usar para guardar su horario (sin formato)", bg = "lightgreen",\
                                font = ("Arial", 9)).grid(row = 8, column = 0)
            boton_guardar_archivo = Button(ventana_entrada, text = "Guardar", bg = "green",\
                                       font = ("Arial", 11), padx = 16, command = boton_guardar).grid(row = 9)
            
            #Aquí se hace una comprobación del color de fondo de debes
            #tener cada texto, dependiendo del bloque en el que esté.
            #en el siguiente bloque se agregan las actividades al horario.
            actividad_get=str(actividad.get())
            #Con este if, lo que haremos será acomodar el texto al tamaño
            #del cuadro, para que no se salga por los bordes, haciendo que
            #el texto se acomode en 3 líneas, de ser necesario.
            if len(actividad_get)>15:
                if len(actividad_get)>30:
                    actividad_aponer=actividad_get[0:15]+"\n"+actividad_get[15:30] \
                                      + "\n" + actividad_get[30:]
                    if (i + j) % 2 == 0:                
                        texto = Label(root2, text = actividad_aponer, bg = "lightgreen",\
                                      font = ("Arial", 8)).grid(row = j, column = i)      
                    else:
                        texto = Label(root2, text = actividad_aponer, bg = "lightblue",\
                                      font = ("Arial", 8)).grid(row = j , column = i)
                        
                else:
                    actividad_aponer=actividad_get[0:15]+"\n"+actividad_get[15:]
                    if (i + j) % 2 == 0:                
                        texto = Label(root2, text = actividad_aponer, bg = "lightgreen",\
                                      font = ("Arial", 8)).grid(row = j, column = i)        
                    else:
                        texto = Label(root2, text = actividad_aponer, bg = "lightblue",\
                                      font = ("Arial", 8)).grid(row = j , column = i)
            else:
                if (i + j) % 2 == 0:                
                    texto = Label(root2, text = actividad.get(), bg = "lightgreen",\
                                  font = ("Arial", 8)).grid(row = j, column = i)
                else:
                    texto = Label(root2, text = actividad.get(), bg = "lightblue",\
                                  font = ("Arial", 8)).grid(row = j , column = i )
            
            # Al lado derecho, estará el botón verde que sirve para guardar
    # los datos ingresados en un archivo .csv

            #Finalmente, el botón de asignar, lo que hace es enviar
            #la actividad ingresada al bloque correspondiente.

        boton_asignar=Button(ventana_entrada,text="Asignar",\
                            command=boton_asignar,bg="green", font = ("Arial", 12))
        boton_asignar.grid(row=2)

    #Primero se creará la ventana en donde se visualizará el horario
    #Esta tendrá un tamaño de 700x665 pixeles.
    root2 =Toplevel()
    root2.title("Horario")
    root2.geometry("700x665")
    
    #Asignación de días, se mostrará el nombre del día a lo largo de la primera fila
    #Para eso se crearán distintos  rectángulos del mismo tamaño, alternando
    #sus colores en un patrón de "ajedrez"

    lunes = Frame(root2)
    textoL = Label(root2, text = "Lunes", bg = "orange", \
                   font = ("Arial",14)).grid(row = 0, column = 1)
    lunes.config(bg = "orange", width = 100, height =  30)
    lunes.grid(row = 0, column = 1)

    martes = Frame(root2)
    textoM = Label(root2, text = "Martes", bg = "darkorange", \
                   font = ("Arial",14)).grid(row = 0, column = 2)
    martes.config(bg = "darkorange", width = 100, height = 30)
    martes.grid(row = 0, column =2)

    miercoles = Frame(root2)
    textoW = Label(root2, text = "Miércoles", bg = "orange",\
                   font = ("Arial",14)).grid(row = 0, column = 3)
    miercoles.config(bg = "orange", width = 100, height = 30)
    miercoles.grid(row = 0, column =3)

    jueves = Frame(root2)
    textoJ = Label(root2, text = "Jueves", bg = "darkorange", \
                   font = ("Arial",14)).grid(row = 0, column = 4)
    jueves.config(bg = "darkorange", width = 100, height = 30)
    jueves.grid(row = 0, column =4)

    viernes = Frame(root2)
    textoV = Label(root2, text = "Viernes", bg = "orange", \
                   font = ("Arial",14)).grid(row = 0, column = 5)
    viernes.config(bg = "orange", width = 100, height = 30)
    viernes.grid(row = 0, column =5)

    sabado = Frame(root2)
    textoV = Label(root2, text = "Sábado", bg = "darkorange", \
                   font = ("Arial",14)).grid(row = 0, column = 6)
    sabado.config(bg = "darkorange", width = 100, height = 30)
    sabado.grid(row = 0, column =6)

    # Asignacion de bloques, se visualizarán en la columna de la izquierda e indicarán el bloque
    # horario correspondiente, para esto se harán varios cuadrados y se irán colocando para
    # abajo

    bloque0 = Frame(root2)
    bloque0.config(bg = "darkorange", width = 100, height = 30)
    bloque0.grid(row = 0, column = 0)
    
    bloque1 = Frame(root2)
    textoB1 = Label(root2, text = "Bloque 1\n08:15-09:35", \
                    bg = "orange", font = ("Arial",12)).grid(row = 1, column = 0)
    bloque1.config(bg = "orange", width = 100, height =  100)
    bloque1.grid(row = 1, column = 0)

    bloque2 = Frame(root2)
    textoB2 = Label(root2, text = "Bloque 2\n09:50-11:10", \
                    bg = "darkorange", font = ("Arial",12)).grid(row = 2, column = 0)
    bloque2.config(bg = "darkorange", width = 100, height = 100)
    bloque2.grid(row = 2, column =0)

    bloque3 = Frame(root2)
    textoB3 = Label(root2, text = "Bloque 3\n11:25-12:45", \
                    bg = "orange", font = ("Arial",12)).grid(row = 3, column = 0)
    bloque3.config(bg = "orange", width = 100, height = 100)
    bloque3.grid(row = 3, column =0)

    bloque4 = Frame(root2)
    textoB4 = Label(root2, text = "Bloque 4\n13:45-15:05", \
                    bg = "darkorange", font = ("Arial",12)).grid(row = 4, column = 0)
    bloque4.config(bg = "darkorange", width = 100, height = 100)
    bloque4.grid(row = 4, column =0)

    bloque5 = Frame(root2)
    textoB5 = Label(root2, text = "Bloque 5\n15:20-16:40", \
                    bg = "orange", font = ("Arial",12)).grid(row = 5, column = 0)
    bloque5.config(bg = "orange", width = 100, height = 100)
    bloque5.grid(row = 5, column =0)

    bloque6 = Frame(root2)
    textoB6 = Label(root2, text = "Bloque 6\n16:55-18:15", \
                    bg = "darkorange", font = ("Arial",12)).grid(row = 6, column = 0)
    bloque6.config(bg = "darkorange", width = 100, height = 100)
    bloque6.grid(row = 6, column =0)

    #Aqui se mostrará la última fila, en donde se agregarán los botones
    #Esta fila se agrerga más que nada por estética, para que no se vea
    #blanco al fondo de la ventana.
    
    fila_botones = Frame(root2)
    fila_botones.config(bg = "orange", width = 100, height = 35)
    fila_botones.grid(row = 7, column = 0)
    
    ultima1 = Frame(root2)
    ultima1.config(bg = "lightgray",width = 100, height = 35)
    ultima1.grid(row = 7, column = 1)

    ultima2 = Frame(root2)
    ultima2.config(bg = "lightgray",width = 100, height = 35)
    ultima2.grid(row = 7, column = 2)
    
    ultima3 = Frame(root2)
    ultima3.config(bg = "lightgray",width = 100, height = 35)
    ultima3.grid(row = 7, column = 3)
    
    ultima4 = Frame(root2)
    ultima4.config(bg = "lightgray",width = 100, height = 35)
    ultima4.grid(row = 7, column = 4)
    
    ultima5 = Frame(root2)
    ultima5.config(bg = "lightgray",width = 100, height = 35)
    ultima5.grid(row = 7, column = 5)

    ultima6 = Frame(root2)
    ultima6.config(bg = "lightgray",width = 100, height = 35)
    ultima6.grid(row = 7, column = 6)
    
    # Aquí abajo se mostrará cada bloque de cada día correspondiente,
    # generando como un sistema de coordenadas, se irán creando 
    # varios cuadrados vacíos, que también tendrán
    # un patrón de ajedrez.

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
    
    # Los botones, en el medio, aparecerá un botón de color
    # cyan, que se encargará de llevar a una nueva ventana, en
    # donde el usuario podrá ingresar sus actividades.
    boton = Button(root2, text = "Agregar", bg= "cyan", font = ("Arial",11), padx=17.5,\
                   pady= 2.1, command = ventana_entra_act).grid(row=7, column = 4)
    # Al lado izquierdo estará el botón rojo de cerrar el programa
    boton_cerrar = Button(root2, text = "Cerrar", command = root.destroy, bg = "red", \
                          fg = "white", padx = 20, font = ("Arial", 11)).grid(row = 7, column = 5)
    boton_recordatorio = Button(root2, text = "Recordatorio", bg= "yellow", font = ("Arial",11), padx=0.8,\
                   pady= 2.1, command = recordatorio).grid(row=7, column = 3)
    
# DEFINICIÓN DE CONSTANTES
# De momento, en nuestro programa no se definió ninguna constante

# BLOQUE PRINCIPAL
 
# ENTRADA

# La entrada está considerada dentro de la función
#ventana_entra_act(), definida más arriba.

# Ventana inicial, incluye una pequeña explicación de lo
#que hace el programa y un botón que lleva a la ventana del horario

# PROCESAMIENTO
root = Tk()
root.title("Entrada")
marco_principal1 = Frame()
texto = Label(root,
              text= "Este programa tiene la finalidad\nde ayudarte a organizar tu horario, para así\n"\
              "mejorar tu rendimiento académico\n y lograr optimizar tu tiempo,\n"\
              "para esto debes pulsar el botón de abajo\n"\
              "para comenzar y cuando se abra \n"\
              "la nueva ventana debes pulsar el botón\n celeste del centro",\
              bg = "pink")

marco_principal1.grid(row=0, column=0)
texto.grid(row=0, column=0)

marco_principal1.config(width = "260", height = "370")
marco_principal1.config(bg = "pink")

boton_inicio = Button(root,text="Comenzar", command=cambia_ventana,\
                      bg="red", width="28", font = ("Arial", 12), fg = "white").grid(row=1,column=0)

# SALIDA
root.mainloop()
