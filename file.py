from random import shuffle
letra= list('ABDEFH')
shuffle(letra)

while letra:
    print(f"Indices disponibles 0 - {len(letra)-1}")
    
    numero = int(input(f"Ingresa un numero entre 0 y {len(letra)-1}: "))

    if 0 <= numero <= len(letra):
        letra_eliminada = letra.pop(numero)
    print(f"ha escogido la forma {letra_eliminada}")