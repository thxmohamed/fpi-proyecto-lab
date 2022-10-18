horario = []

i = 0
while i < 6:
    dia = []
    j = 0
    while j < 6:
        dia.append("[           ]")
        j += 1
    horario.append(dia)
    i += 1

i = 0
while i < 6:
    dia2 = input("Introduzca el día en minúsculas: ")
    dia2.lower()
    if dia2 == "lunes":
        j = 0
        while j < 6:
            bloque = int(input("introduzca el bloque: "))
            if bloque == 1:
                actividad = input("introduzca la actividad: ")
                horario[0][0] = actividad
            elif bloque == 2:
                actividad = input("introduzca la actividad: ")
                horario[0][1] = actividad
            elif bloque == 3:
                actividad = input("introduzca la actividad: ")
                horario[0][2] = actividad
            elif bloque == 4:
                actividad = input("introduzca la actividad: ")
                horario[0][3] = actividad
            elif bloque == 5:
                actividad = input("introduzca la actividad: ")
                horario[0][4] = actividad
            elif bloque == 6:
                actividad = input("introduzca la actividad: ")
                horario[0][5] = actividad
            j += 1
    
    i += 1

k = 0
print("                                       Horario")
print(["Lunes","   Martes","   Miércoles", "Jueves", "  Viernes", "  Sábado"])
while k < len(horario):
    print(horario[k])
    print()
    k += 1
