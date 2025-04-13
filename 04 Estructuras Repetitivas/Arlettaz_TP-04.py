# mostramos todos los numeros del 0 al 100 en orden creciente incluyendo ambos
num = 0
for num in range(0,101):
    print(num)


# pedimos un numero al usuario y calculamos la cantidad de digitos
num2 = str(input("Ingrese un numero entero: "))
print(f"El numero {num2} tiene {len(num2)} digitos")


# pedimos 2 numeros enteros al usuario
print("Ingrese 2 numeros enteros")
num3 = int(input("Primer numero entero: "))
num4 = int(input("Segundo numero entero: "))
suma = 0
# realizamos la suma de todos los numeros entre los 2 numeros dados por el usuario
for i in range(num3,(num4+1)):
    suma = suma + num3
    num3 += 1
print(f"La suma es: {suma}")


# pedimos al usuario que ingrese numeros para hacer una suma en secuencia
print("Ingrese un numero para realizar una suma en secuencia")
# le informamos que para detener la suma ingrese 0
print("Para finalizar ingrese 0 ")
num5 = int(input("Primer numero: "))
suma1 = 0
# se realiza la suma mientras que el numero sea distinto a 0
while num5 != 0:
    suma1 = suma1 + num5
    num5 = int(input("Ingrese otro numero: "))
print(f"El resultado de la suma es {suma1}")


# creamos el numero aleatorio entre 0 y 9
import random
num_azar = random.randint(0,9)
# hacemos que el usuario adivine el numero aleatorio y contamos sus intentos
num_adivinar = int(input("Adivina un numero al azar del 0 al 9: "))
cont = 1
while num_adivinar != num_azar:
    cont += 1
    num_adivinar = int(input("Intenta de nuevo: "))
print(f"Adivinaste el numero en {cont} intentos")


# imprimimos en orden decreciente todos los numeros pares de 100 a 0
for c in range(100,-1,-2):
    print(c)


# pedimos un numero entero al usuario para sumar todos los numeros
# entre 0 y el numero ingresado
num7 = int(input("Ingrese un numero entero: "))
suma2 = 0
num6 = 0
# realizamos la suma y mostramos el resultado
for n in range(num6,(num7+1)):
    suma2 = suma2 + num6
    num6 += 1
print(f"La suma de los numeros entre 0 y {num7} es {suma2}")


# inicializamos todas las variables en 0
cont_numeros = 0
cont_num_par = 0
cont_num_impar = 0
cont_num_negativo = 0
cont_num_positivo = 0
# creamos el bucle que determina cada numero ingresado por el usuario
# en par impar positivo y negativo
while cont_numeros < 100:
    num8 = int(input(f"Ingrese el numero {cont_numeros + 1}: "))
    if num8 % 2 == 0 and num8 < 0:
        cont_num_par += 1
        cont_num_negativo += 1
    elif num8 % 2 == 0 and num8 > 0:
        cont_num_par += 1
        cont_num_positivo += 1
    elif num8 % 2 != 0 and num8 < 0:
        cont_num_impar += 1
        cont_num_negativo += 1
    elif num8 % 2 != 0 and num8 > 0:
        cont_num_impar += 1
        cont_num_positivo += 1
    cont_numeros += 1
# mostramos en pantalla la cantidad de numeros por pares impares positivos y negativos
print(f"Numeros pares: {cont_num_par}")
print(f"Numeros impares: {cont_num_impar} ")
print(f"Numeros positivos: {cont_num_positivo}")
print(f"Numeros negativos: {cont_num_negativo} ")


cont_numeros1 = 0
suma3 = 0
# creamos un bucle donde el usuario debe ingresar 100 numeros enteros
# de los cuales luego los sumamos y calculamos la media
while cont_numeros1 < 100:
    num9 = int(input(f"Ingrese un el numero {cont_numeros1 + 1}: "))
    suma3 = suma3 + num9
    cont_numeros1 += 1
# le mostramos el resultado al usuario
# la media de los 100 numeros que el ingresó
media = suma3 / cont_numeros1
print(f"La media de todos los numeros ingresados es {media}")


# pedimos un numero al usuario
num10 = (input("Ingrese un numero: "))
# invertimos ese numero navegando por la cadena de texto ingresada
# en este caso hacemos que vaya de atras hacia adelante
# lo convertimos en entero y luego lo mostramos en pantalla
num_invertido = int(num10[::-1])
print(f"El numero invertido es {num_invertido}")