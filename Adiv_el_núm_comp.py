import random


def adiv_el_núm_comp(x):

    print("==========================")
    print(" ¡Bienvenido(a) al juego! ")
    print("==========================")
    print(input(f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinar"))

    limite_inferior = 1
    limite_superior = x
    
    respuesta = ""
    while respuesta != "c":
         # Genera prediccion
         if limite_inferior != limite_superior:
             predicción = random.randint(limite_inferior, limite_superior) 
         else:
             predicción = limite_inferior #tambien puede ser el lkimite superior

             #Obtenemos respuesta del usuario
             respuesta = input(f"Mi prediccion es  {predicción}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C)").lower()
              
         if respuesta == "a":
             limite_superior = predicción - 1
         elif  respuesta == "b":
             limite_inferior = predicción + 1

    print(f"¡Siiiiii! La computadora adivino tu numero correctamente: {predicción} ")      


adiv_el_núm_comp (10)                 