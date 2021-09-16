"""
1.1	Simular la administración en la asignación de memoria con particiones variables de DIFERENTES
tamaños para un sistema con 3 procesos P1, P2 y P3.   Se prevé asignar 150 b de memoria al núcleo
del Sistema Operativo. Los procesos tendrán los siguientes tamaños P1= 100 b, P2= 150 b, P3= 250 b.
Luego de la asignación deberá imprimirse la información contenida en una tabla de particiones.
La tabla de particiones contendrá la siguiente información (id Proceso, dirección de comienzo de
la partición asignada, tamaño de la partición).
"""
#aca creamos la particion
def Particion(nomb,cant):
    l=list()
    l=[None]*cant
    a=dict()
    a["nombre"] = nomb
    a["espacio"]=l
    return a
#funcion para juntar las particiones en una lista y la devolverla
def CrearMemoria():
    m = list()  
    m.append(Particion("Sistema Operativo",150))
    m.append(Particion("Particion 1",100))
    m.append(Particion("Particion 2",150))
    m.append(Particion("Particion 3",250))
    return m

#aqui generaremos ls particiones para

def MostrarMemoriaActual(me):
    for j in range(len(me)):
        print("-------------------------------------------------------------------------------")
        print("********",me[j]["nombre"],"********")
        for t in range(len(me[j]["espacio"])//10):
            for i in range(10):
                print(me[j]["espacio"][t], end=" ")
            print()
    print("-------------------------------------------------------------------------------")
    print()



"""memoria = CrearMemoria(700)
GeneracionDeParticiones(memoria)
MostrarMemoriaActual(memoria)"""

memori=CrearMemoria()
MostrarMemoriaActual(memori)
memoriOrdenada= sorted(memori, key=lambda Tpart : Tpart["espacio"])
MostrarMemoriaActual(memoriOrdenada)