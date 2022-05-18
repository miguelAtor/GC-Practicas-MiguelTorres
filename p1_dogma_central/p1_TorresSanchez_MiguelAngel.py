# Genómica Computacional 2022-2
# # Práctica 1. El dogma central de la biología molecular.
# 
# #### Equipo:
# Torres Sánchez Miguel Ángel
# 
# Robles Lara Mariana Jocelyn

# Se necesita tener el archivo "diccionario_codones.py" en el mismo
# directorio que este script para correrlo
from diccionario_codones import codones_traduccion

# Función que revisa si una cadena de DNA ingresada es válida
def valida_cadena(cadena):
    valido = True
    for i in cadena:
        
        if i not in no_valido:
            print("La secuencia de DNA es válida.")
        
        else:
            print("La secuencia de DNA no es válida.")
            valido =  False
            break
    return valido

# Función para obtener la cadena complementaria de otra cadena de DNA 
def obten_complementaria(cadena):
    complementaria = ""
    for a in cadena:
        if a == "G":
            complementaria += "C"
        elif a == "C":
            complementaria += "G"
        elif a == "A":
            complementaria += "T"
        elif a == "T":
            complementaria += "A"
    print("La secuencia complementaria es: ", complementaria)

# Función para transcribir la cadena de DNA a mRNA
def transcribe_cadena(cadena):
    transcrita = ""
    for x in cadena:
        if x == "T":
            transcrita += "U"
        else:
            transcrita += x
    return transcrita

# Función para determinar si la cadena tiene el codón de inicio
def tiene_inicio(cadena):
    if cadena[0:3] == "AUG":
        return True
    else:
        return False

# Función para traducir a la cadena de aminoacidos
def obten_aminoacidos(cadena):
    aminoacidos = ""
    for i in range(3, len(cadena), 3):
        codon = cadena[i:i+3]
        try:
            traduccion = codones_traduccion[codon]
        except:
            traduccion = "-"
        aminoacidos += traduccion
    return aminoacidos


# lista de valores no válidos
no_valido = ["B","D","E","F","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","U","V","W","X","Y","Z"]

cadena = input("Ingresa una cadena de DNA: ")
cadena = cadena.upper() 
if valida_cadena(cadena) == True:
    obten_complementaria(cadena)
    cadena = transcribe_cadena(cadena)
    print("Cadena transcrita (mRNA): " + cadena)
    if tiene_inicio(cadena):
        print("Cadena traducida: " + obten_aminoacidos(cadena))
    else:
        print("No tiene codón de inicio :c")