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