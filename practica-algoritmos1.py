  
'''
// Paso 1: Solicitar entrada al usuario
    Mostrar mensaje: "POr favor, ingrese una palabra: "
    definir variable palabra_ingresada con la lectura de la entrada

    // Paso 2: Contar la cantidad de letras
    Definir la variable cantidad_letras y asignarle la longitud de palabra_ingresada

    //  Paso 3: Mostrar al usuario el resutado
    Mostrar mensaje: "La palabra ingresada tiene:", cantidad_letras, "letras."

'''

# Paso 1 : Solicitar entrada al usuario

palabra_ingresada = input("Por favor, ingrese la palabra: ")

# Paso 2: Contar la cantidad de letras
cantidad_letras = len(palabra_ingresada)

# Paso 3: Mostrar al usuario el resultado

print("La palabra ingresada tiene: ", cantidad_letras, " letras.")