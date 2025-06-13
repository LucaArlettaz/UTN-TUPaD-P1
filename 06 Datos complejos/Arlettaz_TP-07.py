# creamos el diccionario precios_frutas y le agregamos otras 3 frutas
precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# modificamos el precio de 3 frutas existentes 
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# mostramos solo las keys de precios_frutas
lista_frutas = precios_frutas.keys()
print(lista_frutas)

# creamos una agenda de 5 contactos con nombres y numeros
contactos = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el numero de {nombre}: ")
    contactos[nombre] = numero

# consultamos si un nombre esta dentro de nuestros contactos
# y si está, mostramos su numero, si no está, lo informamos
consulta = input("Ingrese el nombre del contacto que busca: ")

if consulta in contactos:
    print(f"El numero de {consulta} es {contactos[consulta]}")
else:
    print(f"{consulta} no está en sus contactos")

# pedimos al usuario que ingrese una frase
# luego averiguamos las palabras unicas de la frase
# palabras que no se repiten
frase = input("Ingrese una frase: ")
frase_palabras = frase.split()
palabras_unicas = set(frase_palabras)
print("Palabras unicas:")
print(palabras_unicas)

# hacemos un recuento de las palabras que hay en la frase y lo mostramos en pantalla
palabras_cant = {}
for palabra in frase_palabras:
    if palabra in palabras_cant:
        palabras_cant[palabra] += 1
    else:
        palabras_cant[palabra] = 1

print("Recuento de palabras:")
print(palabras_cant)

# creamos un diccionario pidiendo al usuario que ingrese alumnos y sus notas
alumnos = {}
for i in range(3):
    nombre_alumno = input(f"Ingresa el nombre del alumno {i+1}: ")
    notas = input(f"Ingresa 3 notas del alumno {nombre_alumno}, separadas por un espacio: ")
    notas = tuple(map(float, notas.split())) # convertimos todas las notas ingresadas en floats, y dentro de una tupla
    alumnos[nombre_alumno] = notas # vamos guardando cada alumno y sus notas en el diccionario

# calculamos el promedio de cada alumno
print("Promedios de cada alumno:")
for nombre_alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas) # el promedio es la suma de las notas divido la cantidad de notas
    print(f"{nombre_alumno}: promedio = {promedio:.2f}") # mostramos 2 decimales luego del numero


# Pedimos listas de estudiantes que aprobaron cada parcial
notas1 = input("Ingresá el numero en la lista de los estudiantes del Parcial 1 que aprobaron: ")
notas2 = input("Ingresá el numero en la lista de los estudiantes del Parcial 2 que aprobaron: ")

# Convertimos a listas de enteros
aprobados1 = set(map(int, notas1.split()))
aprobados2 = set(map(int, notas2.split()))

# Aprobaron ambos
ambos = aprobados1 & aprobados2

# Aprobaron solo uno
solo_uno = aprobados1 ^ aprobados2

# Aprobaron al menos uno
al_menos_uno = aprobados1 | aprobados2

# Mostramos los resultados
print("Aprobaron ambos parciales:")
print(ambos)

print("Aprobaron solo uno de los dos:")
print(solo_uno)

print("Aprobaron al menos un parcial:")
print(al_menos_uno)


# Creamos el diccionario inicial de productos
stock = {"pan": 10, "agua": 5, "galletitas": 15, "huevos": 6, "gaseosas": 8}

# Mostramos los productos disponibles
print("Productos disponibles:", list(stock.keys()))

# Pedimos al usuario un producto a consultar
producto = input("Ingrese el nombre de un producto: ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]} unidades")

    # Le preguntamos si quiere agregar unidades
    opcion = input("Desea agregar unidades a este producto? (si/no): ").lower()
    if opcion == "si":
        cantidad = int(input("¿Cuántas unidades desea agregar?: "))
        stock[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock[producto]} unidades")  # agregamos las unidades que desea el usuario y mostramos resultado
else:
    print(f"{producto} no existe en el stock.")
    # Preguntamos si quiere agregar el nuevo producto
    opcion = input("Desea agregar el producto al stock? (si/no): ").lower()
    if opcion == "si":
        cantidad = int(input("¿Cuántas unidades desea agregar?: "))
        stock[producto] = cantidad
        print(f"Producto {producto} agregado con {cantidad} unidades.")

# Mostramos el stock final
print("Stock actualizado:")
for producto, cantidad in stock.items():
    print(f"{producto}: {cantidad}")


# creamos una agenda vacía
agenda = {}

# pedimos una cantidad de eventos a agendar
cantidad_eventos = int(input("¿Cuántos eventos desea ingresar?: "))

# Pedimos datos al usuario
for i in range(cantidad_eventos):
    dia = input(f"Ingrese el día del evento {i+1}: ").lower()
    hora = input(f"Ingrese la hora del evento {i+1} (formato hh:mm): ")
    evento = input(f"Ingrese la descripción del evento {i+1}: ")

    clave = (dia, hora)
    agenda[clave] = evento

print("Agenda completa:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

# consulta de una actividad
# pedimos al usuario dia y hora que desea consultar
print("Consultar actividad")
consulta_dia = input("Ingrese el día a consultar: ").lower()
consulta_hora = input("Ingrese la hora a consultar (formato hh:mm): ")

consulta_clave = (consulta_dia, consulta_hora)
# si el día y hora que el usuario consulta está en su agenda le informamos el evento
# en caso contrario le informamos que no hay actividad programada
if consulta_clave in agenda:
    print(f"Hay una actividad programada: {agenda[consulta_clave]}")
else:
    print("No hay ninguna actividad programada en ese día y hora.")


# diccionario original sin invertir
paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Italia": "Roma", "Uruguay": "Montevideo", "Brasil": "Brasilia", "España": "Madrid"}
print("Diccionario original")
print(paises)

# creamos un nuevo diccionario invirtiendo clave y valor
# invertimos paises por sus capitales
# creamos otro diccionario llamado capitales
capitales = {}
for pais, capital in paises.items():
    capitales[capital] = pais

# Mostramos el diccionario invertido
print("Diccionario invertido:")
print(capitales)