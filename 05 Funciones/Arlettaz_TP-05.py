listaEj1 = list(range(4,101,4))
print(listaEj1)


ListaEj2 = [True, 12, 2.5, False, "Luca"]
penultimo_elemento = ListaEj2[-2] # indexing negativo -2 para obtener el penultimo
print(penultimo_elemento)


lista_vacia_ej3 = []
lista_vacia_ej3.append("Teclado")
lista_vacia_ej3.append("Ratón")
lista_vacia_ej3.append("Pantalla")

print(lista_vacia_ej3)


animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "Loro"
animales[3] = "Oso"
print(animales)


numeros = [8, 15, 3 , 22, 7]
numeros.remove(max(numeros))
print(numeros) 
# en este programa lo que se realiza es eliminar el maximo numero de la lista numeros
# con un .remove


listaEj6 = list(range(10, 31, 5))
print(listaEj6[:2])


autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "amarok"
autos[2] = "taos"
print(autos)


dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)


compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)


lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)