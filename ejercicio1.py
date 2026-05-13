# Maximo 5 intentos
# randitn (1,50)
# Muy bajo" si el ingresado es menor.
# "Muy alto" si el ingresado es mayor.
# "¡Correcto!" si acierta (y termina el ciclo)

from random import randint
num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
while num2 < num1:
    print("El numero 2 debe ser mayor al numero 1")
    num1 = int(input("Ingrese el numero 1"))
    num2 = int(input("Ingrese el numero 2"))
secreto = randint(num1,num2)
intentos = 1
MAX_INTENTOS = 5
is_not_correct = True
print(f"Debes adivinar un numero entre ({num1} - {num2}) tienes {MAX_INTENTOS} intentos")
while intentos <= MAX_INTENTOS and is_not_correct:
    try:
        numero= int(input(f"Intenteto {intentos}: "))
        while  numero> num2 or numero < num1:
            print (f"el numero debe esta entre {num1} y {num2}")
            numero= int(input(f"Intenteto {intentos}: "))
    except ValueError:
        print("Debes ingresar un numero")
        continue
    print(f"Este es el secreto: {secreto}")
    if(secreto%2!=0 and secreto+1<num2):
        secreto+=1
    elif secreto%2 != 0 :
        secreto -=1

    if numero < secreto:
        print("El numero es Mayor")
    elif numero > secreto:
        print("El numero es menor")
    else:
        print("¡Correcto!")
        is_not_correct= False
    if (intentos == MAX_INTENTOS):
        print(f"El numero secreto era: {secreto}")
    intentos+=1
