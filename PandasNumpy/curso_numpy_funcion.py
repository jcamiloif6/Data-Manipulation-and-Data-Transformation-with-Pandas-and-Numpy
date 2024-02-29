from numpy import random
lista_nombres = ["Alberto", "Alfonso", "Lucia", "Isabel", "Marcos", "Sergio"]

ganador = random.choice(lista_nombres, size=(3, 5))

print(ganador)