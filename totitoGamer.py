from tkinter import Tk,Label,Button,Text#Libreria que utiliza para crear la interfaz del usuario
state=0

#Esta es la ventana principal de la aplicación

ventana=Tk()

#Metodo encargado de hacer la accion al dar clic a los botones
def clic(boton):
    #Aqui decide segun una variable cuando pulsan un clic escoge si mostrar una X o un O en el boton
    if state==0:
        boton.configure(ventana,text="X")
        state=1
    else:
        boton.configure(ventana,text="O")
        state=0


ventana.title("TOTITO GAMER")#Es el titulo de la ventana
ventana.geometry("500x500")#Tamaño de la ventana
Label(ventana,text="BIENVENIDO; VAMOS A JUGAR").grid(row=0,column=0)#Label de bienvenida
#Botones del totito gamer, el metodo command se encarga de dar evento al clic, le damos tamaño de ancho y altura
#Tambien lo vamos a meter a un metodo grid que hace como un ordenamiento para que no este desordenado los botones
#Definimos en que fila y columna van a estar los botones

Button(ventana,command=lambda:clic(Button), height = 10, width = 20,text="").grid(row=1,column=0)
Button(ventana,command=lambda:clic(Button),height = 10, width = 20,text="").grid(row=1,column=2)
Button(ventana,command=lambda:clic(Button),height = 10, width = 20,text="").grid(row=1,column=4)
Button(ventana,command=lambda:clic(Button),height = 10, width = 20,text="").grid(row=2,column=0)
Button(ventana,command=lambda:clic(Button),height = 10, width = 20,text="").grid(row=2,column=2)
Button(ventana,command=lambda:clic(Button),height = 10, width = 20,text="").grid(row=2,column=4)
Button(ventana,command=lambda:clic(Button),height = 10, width = 20,text="").grid(row=3,column=0)
Button(ventana,command=lambda:clic(Button),height = 10, width = 20,text="").grid(row=3,column=2)
Button(ventana,command=lambda:clic(Button),height = 10, width = 20,text="").grid(row=3,column=4)
ventana.mainloop()#Metodo que se encarga en que no se cierre el programa a menos que el usuario pulse el boton de cerrar

