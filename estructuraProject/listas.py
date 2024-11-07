# listas
print("---resultado----")
lista = [1]
print(lista)
lista1 = [1,2,3,4,5,"hola", 4.5]
print(lista1)
print("--------------------------------")


#enlazar las listas
print("---resultado----")
lista2 =[0,1,2,3]
lista3 =["A","B","C"]
lista4= [lista2,lista3]
print(lista4)
print(lista4[1][1])
print("--------------------------------")



#definicion de una lista
print("---resultado----")
lista =[]
lista1=["este es un texto"]
lista2=['es una cadena',123]
lista3=[1,2,3,4,5,'hola','a']
print(lista)
print(lista1)
print(lista2)
print(lista3)
print("--------------------------------")



#concardenacion
print("---resultado----")
lista8 = ["A","B","C","E"]
lista9 = [1,2,3,4,5]
lista10 = lista8 + lista9
print(lista10)
print(lista10[2])
print("--------------------------------")

#el metodo de extend egrega una lista al final de otro listo
print("---resultado----")
nombres1=["duban","carlos","yuli"]
nombres2=["barry","jhoin","guttag"]
nombres1.extend(nombres2)
print(nombres1)
print(nombres2)
print("-----------------------------------------------")


#operaciones con listas
#repetir
print("---resultado----")
lista11=[1,2,3,4,5]
lista12=lista11*3
print(lista12)

print("-----------------------------------------------")

#comparacion
#usando los operadores convencionales
print("---resultado----")
print(["Rojas",123]<["Rojas",123])
print(["Rosas",123]==["rosas",123])
print(["Rosas",123]>["Rosas",123])
print("-----------------------------------------------")

#es posible determinar si un elemneto se encuentra en la lista
print("---resultado----")
lista13 =["cien","años","de","soledad"]
if "de" in lista13:
    print("si esta en la lista")
else:
    print("no esta en la lista")
print("--------------------------------------------------------------")


#interando una lista
print("---resultado----")

lista15 = ["hola","amigos","mios"]
for palabra in lista15:
  print(palabra, end=",")
print("--------------------------------------")

#ejemplo
print("---resultado----")
dirccion = {}
puertos={
    22:"ssh",
    23:"telnet",
    80:"http",
    3306:"MYSQL"
}

print("--------------------------------------------------------")


#el metodo de update agrega items de un diccionario a otro
print("---resultado----")
protocolo = puertos[22]
print(protocolo)
#puertos3[8080]#Error

#Eliminar item con la clave dada
print("---resultado----")
calificaciones = {
    "alumnos1":5,
    "alumnos2":3,
    "alumnos3":4,
    "alumnos4":3
}
print(calificaciones)
del calificaciones ["alumnos3"]
print(calificaciones)

#Iterar un diccionario
#usar el ciclo for y el metodo items para obtener los items de un diccionario.
print("---resultado----")
dicPuertos = {
    22:"SSH",
    23:"Telnet",
    80:"Http"
}
for x,y in dicPuertos.items():
    print(x, "->", y)