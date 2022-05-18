# Genómica Computacional 2022 - Práctica 1. Dogma Central
### Miguel Ángel Torres Sánchez
***

El programa debe pide al usuario una cadena de DNA y el usuario puede ingresar la cadena en minúsculas o mayúsculas.

El programa puede:
- Validar la cadena que ingresa el usuario.
- Arrojar la cadena de DNA complementaria.
- Arrojar la cadena transcrita (mRNA).
- Verficar que la cadena contenga un codón de inicio.
- Arrojar la cadena traducida (cadena de aminoácidos).

Para poder funcionar correctamente el programa debe estar en el mismo directorio que el archivo `diccionario_codones.py`. De este archivo obtiene las traducciones de aminoácidos.

## Funciones
***

### Función `valida_cadenas(cadena)`
Esta función se encarga de validar la cadena de DNA ingresada por el usuario. Imprime el resultado en pantalla y si no es válida termina el programa.

### Función `obten_complementaria(cadena)`
Esta función obtiene la cadena de DNA complementaria de la cadena que recibe como parámetro e imprime en pantalla su resultado.

### Función `transcribe_cadena(cadena)`
Esta funcions se encarga de la transcripción de una cadena de DNA a mRNA. Regresa la cadena transcrita pero no imprime la imprime en pantalla.

### Función `tiene_inicio(cadena)`
Esta función verifica si una cadena inicia con un codón de inicio. Regresa `True` si lo contiene y `False` en caso contrario.

### Función `obten_aminoacidos(cadena)`
Función que traduce la cadena de mRNA a la cadena de aminoácidos respectivos. Para los codones que no codifican a un aminoácido se escribe un guión medio ( `-` ).