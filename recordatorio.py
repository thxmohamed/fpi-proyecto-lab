from datetime import datetime

t_actual= datetime.now()

#fecha
t_bloque1=datetime(t_actual.year,t_actual.month,t_actual.day,8,15,0000)
t_bloque2=datetime(t_actual.year,t_actual.month,t_actual.day,9,50,00,0000)
t_bloque3=datetime(t_actual.year,t_actual.month,t_actual.day,11,25,00,0000)
t_bloque4=datetime(t_actual.year,t_actual.month,t_actual.day,13,45,00,0000)
t_bloque5=datetime(t_actual.year,t_actual.month,t_actual.day,15,20,00,0000)
t_bloque6=datetime(t_actual.year,t_actual.month,t_actual.day,16,55,00,0000)

#hora
hr_bloque1= t_bloque1.hour
hr_bloque2= t_bloque2.hour
hr_bloque3= t_bloque3.hour
hr_bloque4= t_bloque4.hour
hr_bloque5= t_bloque5.hour
hr_bloque6= t_bloque6.hour

#minuto
min_bloque1 = t_bloque1.minute
min_bloque2 = t_bloque2.minute
min_bloque3 = t_bloque3.minute
min_bloque4 = t_bloque4.minute
min_bloque5 = t_bloque5.minute
min_bloque6 = t_bloque6.minute

#tiempo para prox actividad,se podria mostrar en pantalla

if t_actual < t_bloque1:
        t_restante= t_actual-t_bloque1
        t_restante=abs(t_restante)
        print(t_restante)
elif t_actual < t_bloque2:
        t_restante= t_actual-t_bloque2
        t_restante=abs(t_restante)
        print(t_restante)
elif t_actual < t_bloque3:
        t_restante= t_actual-t_bloque3
        t_restante=abs(t_restante)
        print(t_restante)
elif t_actual < t_bloque4:
        t_restante= t_actual-t_bloque4
        t_restante=abs(t_restante)
        print(t_restante)
elif t_actual < t_bloque5:
        t_restante= t_actual-t_bloque5
        t_restante=abs(t_restante)
        print(t_restante)
elif t_actual < t_bloque6:
        t_restante= t_actual-t_bloque6
        t_restante=abs(t_restante)
        print(t_restante)


#hago el t_restante una lista para operar con las horas y minutos de este
lista_trestante= str(t_restante).split(":")
print(lista_trestante)


#aviso 10 min antes
if lista_trestante[0] == 0 and lista_trestante[1] == 10:
    print("quedan 10 min para (actividad-x)") #podria saltar una ventana de aviso del tkinter
    

#abs() parar tiempos
