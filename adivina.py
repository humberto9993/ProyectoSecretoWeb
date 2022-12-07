import random

# Generamos un número aleatorio entre 1 y 100
numero_a_adivinar = random.randint(1, 100)

# Pedimos al usuario que adivine el número
adivinanza = int(input("Adivina el número (entre 1 y 100): "))

# Mientras la adivinanza no sea correcta, seguimos pidiendo adivinanzas
while adivinanza != numero_a_adivinar:
  # Si la adivinanza es mayor que el número a adivinar, decimos que el número es más pequeño
  if adivinanza > numero_a_adivinar:
    print("El número es más pequeño")
  # Si la adivinanza es menor que el número a adivinar, decimos que el número es más grande
  else:
    print("El número es más grande")
    
  # Pedimos otra adivinanza
  adivinanza = int(input("Adivina otra vez: "))
  
# Si llegamos a este punto, es porque la adivinanza fue correcta
print("¡Felicidades! Adivinaste el número")
