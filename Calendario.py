#Funciones
def interseccion_horas(dia):
    i = 0
    while i < len(dia):
        j = 1
        while j < len(dia)-i:
            if dia[i][0][0] >= dia[j][0][0] and  dia[i][0][1] <= dia[j][0][0]:
                return print(("Sus horarios no son compatibles..."))
            elif dia[j][0][1] >= dia[i][0][0] and  dia[j][0][1] <= dia[i][0][1]:
                return print(("Sus horarios no son compatibles..."))
            elif dia[i][0][0] >= dia[j][0][0] and  dia[i][0][0] <= dia[j][0][1]:
                return print(("Sus horarios no son compatibles..."))
            elif dia[j][0][0] <= dia[i][0][1] and  dia[j][0][1] >= dia[i][0][1]:
                return print(("Sus horarios no son compatibles...")) 
            j = j + 1
        i = i + 1
def hora_correcta(dia):
    i = 0
    while i < len(dia):
        dos_puntos = dia[i][0][0].find(":")
        if float(dia[i][0][0][0:dos_puntos]) >= 24:
            return print("Sus horarios no están bien escritos...")
        if float(dia[i][0][0][dos_puntos + 1:]) >= 60:
            return print("Sus horarios no están bien escritos...")
        dos_puntos = dia[i][0][1].find(":")
        if float(dia[i][0][1][0:dos_puntos]) >= 24:
            return print("Sus horarios no están bien escritos...")
        if float(dia[i][0][1][dos_puntos + 1:]) >= 60:
            return print("Sus horarios no están bien escritos...")
        i = i + 1
def agregar_cero(dia):
    for i in dia:
        dos_puntos = i[0][0].find(":")
        if len(i[0][0][:dos_puntos]) < 2:
            i[0][0] = "0" + i[0][0]
        if len(i[0][1][:dos_puntos]) < 2:
            i[0][1] = "0" + i[0][1]
    return (dia)
#Entrada
Lunes=[]
Martes=[]
Miercoles=[]
Jueves=[]
Viernes=[]
Sabado=[]
Domingo=[]
switch = True
while switch:
    dia = int(input("Escriba el día de la semana al que quiere agregar horario\n\
con números enteros del 1 al 7, empezando del lunes hasta el domingo: "))
    hora = input("Escriba la hora de inicio y de término de la actividad: ").split(" ")
    actividad = input("Escriba la actividad a realizar: ")
    if dia == 1:
        Lunes.append([hora, actividad])
        interseccion_horas(Lunes)
        hora_correcta(Lunes)
        agregar_cero(Lunes)
    elif dia == 2:
        Martes.append([hora, actividad])
    elif dia == 3:
        Miercoles.append([hora, actividad])
    elif dia == 4:
        Jueves.append([hora, actividad])
    elif dia == 5:
        Viernes.append([hora, actividad])
    elif dia == 6:
        Sabado.append([hora, actividad])
    elif dia == 7:
        Domingo.append([hora, actividad])
    else:
        print("Por favor, ingrese el horario bien...")
    aux = bool(int(input("¿Quiere agregar más datos?: (Escriba 1 si sí y 0 si no)")))
    switch = bool(int(aux))
#Proceso
interseccion_horas(Lunes)
interseccion_horas(Martes)
interseccion_horas(Miercoles)
interseccion_horas(Jueves)
interseccion_horas(Viernes)
interseccion_horas(Sabado)
interseccion_horas(Domingo)
