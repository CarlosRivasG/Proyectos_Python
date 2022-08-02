import random


def adivina_el_número(x):

    print("==========================")
    print(" ¡Bienvenido(a) al juego! ")
    print("==========================")
    print("Tu meta es adivinar el número generado por la computadora")

    número_aleatorio = random.randint(1, x) # Número aleatorio entre 1 y x.

    predicción = 0

    while predicción !=   número_aleatorio:
    #el usuario ingr5esa un numero
   
        predicción = int(input(f"Adivina un número entre 1 y {x}: ")) # cadena de caracteres f-string
        if predicción < número_aleatorio: 
            print("Intenta otra vez. Este número es muy pequeño.")
        elif predicción > número_aleatorio: 
            print("Intenta otra vez, este número es muy alto.")    
    print(f"¡Felicitaciones! Adivinaste el numero {número_aleatorio} correctamente ")        


adivina_el_número(100)
