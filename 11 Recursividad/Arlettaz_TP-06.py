def factorial(n):
    if n == 0 or n == 1:  
        return 1     #Caso base
    else:
        return n * factorial(n-1)

#Pedimos un número al usuario
num_fact = int(input("Ingresa un número entero positivo: "))

#Mostramos los factoriales del 1 al número ingresado
for i in range(1, num_fact + 1):
    print(f"{i} = {factorial(i)}")



def fibonacci(n):
    if n == 0:
        return 0  
    elif n == 1:
        return 1  #Casos base
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Pedimos posición de fibonacci
num_fibonacci = int(input("Ingresa una posición para la serie de Fibonacci: "))

#Mostramos la serie completa hasta el final
print("Serie de Fibonacci:")
for i in range(num_fibonacci + 1):
    print(f"F({i}) = {fibonacci(i)}")



def potencia(n, m):
    if m == 0:
        return 1  #Caso base
    else:
        return n * potencia(n, m-1)

#Pedimos base y exponente al usuario
n = int(input("Ingresa la base: "))
m = int(input("Ingresa un exponente entero positivo: "))

#Mostramos el resultado
resultado = potencia(n, m)
print(f"{n}^{m} = {resultado}")



def decimal_a_binario(n):
    if n == 0:
        return ""  #Caso base
    else:
        return decimal_a_binario(n//2) + str(n % 2)

#Solicitamos un número al usuario
num_decimal = int(input("Ingresa un número entero positivo: "))

if num_decimal == 0:
    num_binario = "0"
else:
    num_binario = decimal_a_binario(num_decimal)

print(f"El número {num_decimal} en binario es: {num_binario}")



def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True  #Caso base: No hay palabra o tiene una sola letra
    elif palabra[0] != palabra[-1]:
        return False  #Caso base: Los extremos no son iguales
    else:
        return es_palindromo(palabra[1:-1])    #Al llegar aca ya sabemos que
                                               #la primer y ultima letra son iguales
#Solicitamos una palabra al usuario
palabra = input("Ingresa una palabra en minusculas sin espacios ni tildes: ")

#Mostramos resultado
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')



def suma_digitos(n):
    if n == 0:
        return 0  #Caso base
    else:
        return (n % 10) + suma_digitos(n // 10)

#Pedimos un numero al usuario y realizamos la suma de los digitos
num_suma_digitos = int(input("Ingresa un número entero positivo: "))
resultado_suma_digitos = suma_digitos(num_suma_digitos)
print(f"La suma de los dígitos de {num_suma_digitos} es: {resultado_suma_digitos}")



def contar_bloques(n):
    if n == 1:
        return 1  #Caso base
    else:
        return n + contar_bloques(n - 1)

#Solicitamos la cantidad de bloques del nivel mas bajo al usuario
bloques_nivel_bajo = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))

#Mostramos el resultado, la cantidad total de bloques
total_bloques = contar_bloques(bloques_nivel_bajo)
print(f"El total de bloques en la pirámide es: {total_bloques}")



def contar_digito(numero, digito):
    if numero == 0:
        return 0  #Caso base
    else:
        #Compara el ultimo digito y lo suma solo si coincide
        return (1 if (numero % 10 == digito) else 0) + contar_digito(numero // 10, digito)

#Pedimos un numero al usuario y un digito que quiera saber cuantas veces aparece en dicho numero
num_completo = int(input("Ingresa un número entero positivo: "))
digito_buscado = int(input("Ingresa un dígito (0-9) para contar: "))

if digito_buscado < 0 or digito_buscado > 9:
    print("El dígito debe estar entre 0 y 9.")
else:
    cant_digito_repetido = contar_digito(num_completo, digito_buscado)
    print(f"El dígito {digito_buscado} aparece {cant_digito_repetido} veces en el número {num_completo}.")