from tkinter import *

root = Tk()



#definios la funcion 
def click_buttom():
    '''la funcion permite generar un cuadro para que el usuario escriba un
       recordatorio'''
    entrada = Entry(root, width=60, bg="yellow", fg="firebrick", borderwidth=10)
    entrada.insert(0,"Escriba aqui...")
    entrada.grid(row= "0", column="1")

    boton_guardar = Button(root,text="GUARDAR", bg= "orange", padx= 50, pady= 10,
                          command= click_buttom2).grid(row="1",column="1")
    return click_buttom

def click_buttom2():
    texto= Label(root, text="el texto ha sido guardado exitosamente").grid(row="2",column="1")
        
#botones
boton = Button(root, text ="QUIERO ESCRIBIR\n UN RECORDATORIO", bg= "lightblue",
               padx= 105, pady= 50, command= click_buttom).grid(row="0",column="0")




root.mainloop
