# Excelente ejemplo de como se pueden concadenar cadenas de caracteres.
# Supongamnos que queremos crear una cadena que diga
# Aprende a programar con ________.

# organización = "freeCodeCamp"

# print("Aprende a programar con " + organización)
# print("Aprende a programar con {}".format(organización))
# print(f"Aprende a programar con {organización}") #f-string



adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (plural): ")

madlib = f"¡Programar es tan {adj}! Siempre me emociona por que me encanta {verbo1} problemas. ¡Aprende a {verbo2}con FreeCodeCamp y alcanza tus {sustantivo_plural}" 

print(madlib)