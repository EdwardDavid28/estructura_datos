#las tuplas
tupla1=()#Tupla vacia

print(tupla1)

tupla2=("Esto es un texto",) #una tupla con un elemento que es una cadena,
print(tupla2)
tupla3=("Una cadena", 128)#una tupla con dos elementos
print(tupla3)
tupla4=("apple", 2018, "samsung", 4.9, True) #una tupla de seis elementos
print(tupla4)

# una tupla heterogenea
tupla4=("apple", 2018,4.9, True)
print(tupla4)
print(tupla4[1])#acceder al elemento de la tupla
print(tupla4[2])


tupla3 = (0,1,2,3)
tupla4= ("A","B","C")
tubla5=(tupla3,tupla4)
print(tubla5)
print(tubla5[1][1])
print(tubla5[1][0])
print(tubla5[0][3])
print("------------------------------------------------")
print("----resultado----")
#OPERACIONES CON TUPLAS SUMA
tupla6 = (0,1,2,3)
tupla5= ("A","B","C")
tubla7=(tupla5+tupla6)
print(tubla7)
print(tubla7[3])

print("------------------------------------------------")
print("----resultado----")
#OPERACIONES CON TUPLAS MULTIPICACION
tupla11 = (0,1,2,3)
tubla12=tupla11*3
print(tubla12)
print("------------------------------------------------")


print("----resultado----")
#compara una tupla
tupla13 = ("Rojas",)
tupla14 =(123,)
tupla15 = ("Rosas",)
tupla16 =("rosas",)
print((tupla13, tupla14)< (tupla15, tupla16))
print((tupla15, tupla16)== (tupla13, tupla14))

print("-----------------------------------------------------")