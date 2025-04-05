# pedimos la edad al usuario
edad = int(input("Ingrese su edad: "))
# averiguamos si el usuario es mayor de edad
if edad > 18:
    print("Es mayor de edad")


# pedimos que el usuario ingrese su nota
nota = int(input("Ingrese su nota: "))

# verificamos a partir de la nota que el usuario ingresó, si aprobó o no.
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# pedimos al usuario que ingrese un numero par
numero = int(input("Ingrese un número par: "))

# verificamos si el número que ingresó es par y se lo decimos, tambien en el caso contrario
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


    # solicitamos al usuario a que ingrese su edad
edad1 = int(input("Ingrese su edad: "))

# le comunicamos al usuario a que categoria pertenece segun su edad
if edad1 < 12:
    print("Usted es Niño/a")
elif edad1 >= 12 and edad1 < 18:
    print("Usted es Adolescente")
elif edad1 >= 18 and edad1 <= 30:
    print("Usted es Adulto/a joven")
else:
    print("Usted es Adulto/a mayor")


# pedimos al usuario que ingrese una contraseña válida
# escribo password porque contraseña contiene Ñ
password = (input("Ingrese una contraseña de entre 8 y 14 caracteres: "))

# verificamos si la contraseña contiene entre 8 y 14 caracteres
# y le comunicamos al usuario el resultado
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


# añadimos las librerias requeridas
from statistics import mode, median, mean
import random 
# generamos 50 numeros aleatorios de entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

# sacamos la moda, mediana y media de los numeros aleatorios
moda = mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)
media = mean (numeros_aleatorios)

# verificamos si hay sesgo positivo, negativo o si no lo hay
if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif moda == mediana and mediana == media:
    print("No hay sesgo")


# solicitamos al usuario una palabra o frase
frase = str(input("Ingrese una palabra o frase: "))
vocales = "AEIOUÁÉÍÓÚaeiouáéíóú"

# si la letra final de la palabra o frase es una vocal le añadimos un !
# sino, lo dejamos como está
if frase[-1] in vocales:
    print(f"{frase}!")
else:
    print(frase)


# pedimos al usuario que ingrese su nombre
nombre = str(input("Ingrese su nombre: "))
# le informamos al usuario las opciones disponibles
print("1. Si quiere su nombre en mayusculas")
print("2. Si quiere su nombre minusculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")
# le damos a elegir la opcion
opcion = int(input("Ingrese un número según lo que desee: "))

# transormamos el nombre del usuario en lo que el desee
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())


# le pedimos al usuario que ingrese la magnitud de un terremoto
magnitud_Terremoto = float(input("Ingrese la magnitud de un terremoto: "))

# clasificamos el terremoto segun la magnitud ingresada
if magnitud_Terremoto < 3:
    print("Muy leve")
elif magnitud_Terremoto >= 3 and magnitud_Terremoto < 4:
    print("Leve")
elif magnitud_Terremoto >= 4 and magnitud_Terremoto < 5:
    print("Moderado")
elif magnitud_Terremoto >= 5 and magnitud_Terremoto < 6:
    print("Fuerte")
elif magnitud_Terremoto >= 6 and magnitud_Terremoto < 7:
    print("Muy fuerte")
elif magnitud_Terremoto >= 7:
    print("Extremo")


# le solicitamos al usuario que nos diga en que hemisferio se encuentra
print("Opciones de hemisferio: Norte es 1 y Sur es 2")
hemisferio = int((input("¿En que hemisferio se encuentra?: ")))
# le solicitamos al usuario que nos diga en que mes se encuentra
print("Opciones de meses: del 1 al 12")
mes = int(input("Indique en que mes del año se encuentra: "))
# le solicitamos al usuario que nos diga en que dia se encuentra
dia = int(input("Indique que dia del mes es: "))

# le indicamos al usuario en que estacion del año está segun sus datos (hemisferio norte)
if hemisferio == 1:
    if (mes == 12 and 21 <= dia <= 31) or (mes == 1 and 1 <= dia <= 31) or (mes == 2 and 1 <= dia <= 28) or (mes == 3 and 1 <= dia <= 20):
        print("Es invierno")
    elif (mes == 3 and 21 <= dia <= 31) or (mes == 4 and 1 <= dia <= 30) or (mes == 5 and 1 <= dia <= 31) or (mes == 6 and 1 <= dia <= 20):
        print("Es primavera")

    elif (mes == 6 and 21 <= dia <= 30) or (mes == 7 and 1 <= dia <= 31) or (mes == 8 and 1 <= dia <= 31) or (mes == 9 and 1 <= dia <= 20):
        print("Es verano")
    
    else:
       print("Es otoño")
# le indicamos al usuario en que estacion del año está segun sus datos (hemisferio sur)
else:
    if (mes == 12 and 21 <= dia <= 31) or (mes == 1 and 1 <= dia <= 31) or (mes == 2 and 1 <= dia <= 28) or (mes == 3 and 1 <= dia <= 20):
       print("Es verano")
    
    elif (mes == 3 and 21 <= dia <= 31) or (mes == 4 and 1 <= dia <= 30) or (mes == 5 and 1 <= dia <= 31) or (mes == 6 and 1 <= dia <= 20):
        print("Es otoño")

    elif (mes == 6 and 21 <= dia <= 30) or (mes == 7 and 1 <= dia <= 31) or (mes == 8 and 1 <= dia <= 31) or (mes == 9 and 1 <= dia <= 20):
        print("Es invierno")
    
    else:
       print("Es primavera")