import random

# Palabras posibles para el juego
palabras = ['perro', 'gato', 'computadora', 'celular', 'mesa', 'silla']

# Se elige una palabra al azar
palabra_elegida = random.choice(palabras)

# La palabra a adivinar se muestra con guiones bajos
palabra_adivinar = ['_' for i in range(len(palabra_elegida))]

# Se inicia con 6 intentos
intentos_restantes = 6

# Mientras queden intentos y la palabra no haya sido adivinada
while intentos_restantes > 0 and '_' in palabra_adivinar:
    # Se pregunta al usuario por una letra
    letra = input('Ingresa una letra: ')

    # Se verifica si la letra está en la palabra
    if letra in palabra_elegida:
        # Si la letra está en la palabra, se reemplazan los guiones bajos
        # correspondientes
        for i, c in enumerate(palabra_elegida):
            if c == letra:
                palabra_adivinar[i] = letra

        print(f'¡Bien! La letra "{letra}" si está en la palabra.')
    else:
        # Si la letra no está en la palabra, se resta un intento
        intentos_restantes -= 1
        print(f'La letra "{letra}" no está en la palabra.')

    # Se muestra la palabra a adivinar
    print(' '.join(palabra_adivinar))

# Si se agotaron los intentos, se muestra que se perdió
if intentos_restantes == 0:
    print('¡Perdiste! La palabra era:', palabra_elegida)
else:
    # Si se adivinó la palabra, se muestra que se ganó
    print('¡Felicidades! ¡Adivinaste la palabra!')
