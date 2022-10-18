#Funciones
def interseccion_horas(dia):
    i = 0
    while i < len(dia):
        j = 0
        while j < len(dia):}
            if dia[i][0][0] <= dia[j][0][0] and  dia[i][0][1] >= dia[j][0][0]:
                return ("Sus horarios no son compatibles...")
            elif dia[j][0][0] <= dia[i][0][0] and  dia[j][0][1] >= dia[i][0][0]:
                return ("Sus horarios no son compatibles...")
            elif dia[i][0][0] <= dia[j][0][1] and  dia[i][0][1] >= dia[j][0][1]:
                return ("Sus horarios no son compatibles...")
            elif dia[j][0][0] <= dia[i][0][1] and  dia[j][0][1] >= dia[i][0][1]:
                return ("Sus horarios no son compatibles...")
            j = j + 1
        i = i + 1
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
    dia = input("Escriba el día de la semana al que quiere agregar horario: ")
    hora = input("Escriba la hora de inicio y de término de la actividad: ").split(" ")
    actividad = input("Escriba la actividad a realizar: ")
    if dia.lower == "lunes":
        Lunes.append([hora, actividad])
    elif dia.lower == "martes":
        Martes.append([hora, actividad])
    elif dia.lower == "miércoles" or dia.lower == "miercoles":
        Miercoles.append([hora, actividad])
    elif dia.lower == "jueves":
        Jueves.append([hora, actividad])
    elif dia.lower == "viernes":
        Viernes.append([hora, actividad])
    elif dia.lower == "sabado" or dia.lower == "sábado":
        Sabado.append([hora, actividad])
    elif dia.lower == "domingo":
        Domingo.append([hora, actividad])
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
