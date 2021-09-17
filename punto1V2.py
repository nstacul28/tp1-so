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
    a["espacio"] = l
    return a

#funcion para crear las particiones en una lista y la devolverla
def CrearMemoria():
    m = list()  
    m.append(Particion("Sistema Operativo",150))
    m.append(Particion("Particion 1",100))
    m.append(Particion("Particion 2",150))
    m.append(Particion("Particion 3",250))
    return m

#aqui mostramos la memoria con un formato mas lindo a la vista
def MostrarMemoriaActual(me):
    for j in range(len(me)):
        print("-------------------------------------------------------------------------------")
        print("********",me[j]["nombre"],"********")
        for t in range(len(me[j]["espacio"])//10):
            for i in range(10):
                print(me[j]["espacio"][t*10+i], end=" ")
            print()
    print("-------------------------------------------------------------------------------")
    print()

#resta funcion rellena la particion no importa cul sea con el dato, la cant de lugares
def RellenarParticion(part,desde,dato,cant):
    for i in range(desde,(cant+desde)):
        part[i]=dato

#devuelve la max cantidad de lugarases continuos de la memoria libre en el [0] 
#y el lugar donde empieza a estar libre esa maxima cantidad en el [1]
#  , pasando como parametro la lista de la particion
def MaximoLugarDisponible(part):
    c=0
    l=0
    b=True
    for i in range(len(part)):
        if part[i]==None:
            if b:
                l=i
                b=False
            c=c+1
        else:
            c=0
            b=True
    return c,l

def Proceso(nombre,tamaño):
    a=dict()
    a["nombre"] = nombre
    a["tamaño"] = tamaño
    a["usado"] = False
    a["id"] = id(a)
    return a

def CrearProcesos():
    p=list()
    p.append(Proceso("proceso 1",90))
    p.append(Proceso("proceso 2",130))
    p.append(Proceso("proceso 3",200))
    p.append(Proceso("proceso 4",130))
    return p

def IniciarSO(me):
    for i in range(len(me)):
        if me[i]["nombre"]=="Sistema Operativo":
          RellenarParticion(me[i]["espacio"],0,"SO",len(me[i]["espacio"]))


#ordenar los procesos de menor a mayor?








#                                    programa General
memori=CrearMemoria()
#ordenar las particiones de menor a mayor tamaño de memoria
memori= sorted(memori, key=lambda Tpart : Tpart["espacio"])
IniciarSO(memori)
MostrarMemoriaActual(memori)
"""MostrarMemoriaActual(memori)
RellenarParticion(memori[0]["espacio"],20,"p1",30)
MostrarMemoriaActual(memori)
print(memori[0]["espacio"])
print(MaximoLugarDisponible(memori[0]["espacio"]))"""
procesos=CrearProcesos()
print(procesos)
print(MaximoLugarDisponible(memori[1]["espacio"]))

for i in range(len(procesos)):
    #while not procesos[i]["usado"]:
    for j in range(len(memori)):
        print(j)
        if procesos[i]["tamaño"]<=MaximoLugarDisponible(memori[j]["espacio"])[0]:
            print("puse ",procesos[i]["nombre"])
            RellenarParticion(memori[j]["espacio"],MaximoLugarDisponible(memori[j]["espacio"])[1],procesos[i]["nombre"],procesos[i]["tamaño"])
            procesos[i]["usado"]=True
            break            
    if not procesos[i]["usado"]:
        print("El proceso debe esperar")

print(procesos)
MostrarMemoriaActual(memori)
