#definicion de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

#programa principal
imprimir_hola_mundo()

#definicion de funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#programa principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#definicion de funciones
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre,apellido,edad,residencia)

#definicion de funciones
def calcular_area_circulo(radio):
    area = 3.1416 * radio**2
    print(f"El area del circulo es {area}")

def calcular_perimetro_circulo(radio):
    perimetro = (2*3.1416 * radio)
    print(f"El perimetro del circulo es {perimetro}")

#programa principal
radio = float(input("Ingrese el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#definicion de funciones
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos son {horas} horas")
#programa principal
segundos = int(input("Ingrese una cantidad de segundos: "))
segundos_a_horas(segundos)

#definicion de funciones
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

#programa principal
numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

#definicion de funciones
def operaciones_basicas(a, b):
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")

#programa principal
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
operaciones_basicas(a, b)

#definicion de funciones
def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    print(f"El imc es {imc}")

#programa principal
peso = float(input("Ingrese un peso en kilogramos: "))
altura = float(input("Ingrese una altura en metros: "))
calcular_imc(peso, altura)

#definicion de funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celcius * 9/5) + 32
    print(f"{celcius} grados celcius equivalen a {fahrenheit} grados fahrenheit")

#programa principal
celcius = float(input("Ingrese una temperatura en grados celcius: "))
celsius_a_fahrenheit(celcius)

#definicion de funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de estos 3 numeros es {promedio}")

#programa principal
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
calcular_promedio(a,b,c)