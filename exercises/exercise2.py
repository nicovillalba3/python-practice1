import os

"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

esta_lloviendo = True
riego_activado = True
piso_mojado = True

# COMPLETAR - INICIO

if (((esta_lloviendo or riego_activado) or piso_mojado) == True):
    resultado = True
else:
    resultado = False

print(f"Todas las condiciones son: {resultado}.")

    

# COMPLETAR - FIN

assert piso_mojado

os.system("pause")


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

# COMPLETAR - INICIO

if (area_cuadrado > 5):
    area_mayor_a_cinco = not False
    print(f"El area del cuadrado es mayor a 5: {area_mayor_a_cinco}.")
else:
    area_mayor_a_cinco = False
    print(f"El area del cuadrado es mayor a 5: {area_mayor_a_cinco}.")


# COMPLETAR - FIN

assert area_mayor_a_cinco

os.system("pause")



"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50

# COMPLETAR - INICIO

if ((numero_1 % 7) == 0 and (numero_2 % 7) != 0):
    resultado = True
    print(f"La consigna es: {resultado}")
else:
    resultado = False
    print(f"La consigna es: {resultado}")

# COMPLETAR - FIN

assert resultado

os.system("pause")

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
el mismo valor de la variable 3.
Restricción: sólo usar OR, NOT y el mecanismo de cortocircuito.
"""

variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = "90"
variable_05 = 100

# COMPLETAR - INICIO

if (((not variable_01 or variable_02) or (not variable_04 or variable_05) or variable_03)):
    resultado = variable_03

    print(f"El resultado es: {resultado}")

else:
    print(f"Este no es el resultado correcto.")

# COMPLETAR - FIN

assert resultado == 80

os.system("pause")