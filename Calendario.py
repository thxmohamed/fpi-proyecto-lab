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
    a = input("¿Quiere agregar más datos?: (Escriba 1 si sí y 0 si no)")
    switch = bool(int(a))
