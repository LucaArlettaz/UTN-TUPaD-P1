print("Hola Mundo!")

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

nombre1 = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre1} {apellido}, tengo {edad} años y vivo en {lugar}")

radio = float(input("Ingrese el radio de un circulo: "))
print("El área del circulo es ", (3.14159*radio**2), "y el perimetro del circulo es ", (2*3.14159*radio))


segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos/3600
print(f"{segundos} son {horas} horas")

numero1 = int(input("Ingrese un numero: "))
print(f"{numero1} por 1 es {numero1*1}")
print(f"{numero1} por 2 es {numero1*2}")
print(f"{numero1} por 3 es {numero1*3}")
print(f"{numero1} por 4 es {numero1*4}")
print(f"{numero1} por 5 es {numero1*5}")
print(f"{numero1} por 6 es {numero1*6}")
print(f"{numero1} por 7 es {numero1*7}")
print(f"{numero1} por 8 es {numero1*8}")
print(f"{numero1} por 9 es {numero1*9}")
print(f"{numero1} por 10 es {numero1*10}")

numero2 = int(input("Ingrese un numero entero distinto a 0: "))
numero3 = int(input("Ingrese otro numero entero distinto a 0: "))

print(f"{numero2} + {numero3} es {numero2+numero3}")
print(f"{numero2} - {numero3} es {numero2-numero3}")
print(f"{numero2} * {numero3} es {numero2*numero3}")
print(f"{numero2} / {numero3} es {numero2/numero3}")

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / (altura**2)

print(f"Su indice de masa corporal es {imc}")

temperaturaC = float(input("Ingrese una temperatura en grados celcius: "))
temperaturaF = 9/5 * temperaturaC + 32
print(f"{temperaturaC} grados celcius equivalen a {temperaturaF} grados fahrenheit")

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los 3 numeros es {promedio}")