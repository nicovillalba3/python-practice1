import os

"""Comparación"""

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si 2 personas tienen el mismo nombre pero distinta edad.
Aclaración: Se puede utilizar and, or y not.
"""

persona_01 = "Kevin"
edad_01 = 24
persona_02 = "Kevin"
edad_02 = 41

# COMPLETAR - INICIO

nombre_01 = persona_01.lower()
nombre_02 = persona_02.lower()

if ((persona_01 == persona_02) and (edad_01 != edad_02)):
    comparar_nombre_y_edad = True

    print(f"Tanto {persona_01} como {persona_02} tienen el mismo nombre, y sus edades son {edad_01} y {edad_02} respectivamente.")

else:
    print(f"Así ser verían los nombre pasados a minuscula: {nombre_01} y {nombre_02}.")




# COMPLETAR - FIN

assert comparar_nombre_y_edad

os.system("pause")

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si un auto no es de marca Ford y su modelo es igual o anterior al año 2000.
Aclaración: Se puede utilizar and, or y not.
"""

marca_del_auto = "Chevrolet"
modelo_de_auto = 1998

# COMPLETAR - INICIO

if ((marca_del_auto != "Ford") and (modelo_de_auto <= 2000)):
    comparar_marca_y_modelo = True

    print(f"La marca del auto NO es Ford, es: {marca_del_auto} y el modelo es: {modelo_de_auto}. Por lo tanto el resultado es: {comparar_marca_y_modelo}")
else:
    comparar_marca_y_modelo = False
    print(f"La marca del auto SI es {marca_del_auto} y el modelo del auto es: {modelo_de_auto}. Por lo tanto el resultado es: {comparar_marca_y_modelo}")

# COMPLETAR - FIN

assert comparar_marca_y_modelo

os.system("pause")

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si la superfice del campo 1 es menor a la del campo 2 y la superficie del
campo 2 es mayor a la del campo 3.
Restricción: Utilizar comparaciones encadenadas - No utilizar and, or ni not.
"""

superficie_de_campo_01 = 85121
superficie_de_campo_02 = 851212
superficie_de_campo_03 = 8512

# COMPLETAR - INICIO

if (superficie_de_campo_01 < superficie_de_campo_02 > superficie_de_campo_03):

    ##if(superficie_de_campo_02 > superficie_de_campo_03):
        comparar_superficie = True

        print(f"La superficie del campo 01 es mayor a la del campo 02.")
        print(f"Además la superficie del campo 02 es mayor a la del campo 03.")
    ##else:
    ##    comparar_superficie = False
    ##   print(f"La superficie del campo 01 es menor a la del campo 02 y éste último es menor al campo 03.")
else:
    comparar_superficie = False
    print(f"¿La superficie del campo 01 es mayor a la del campo 02?: {comparar_superficie}")


# COMPLETAR - FIN

assert comparar_superficie

os.system("pause")


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si la cantidad de bananas es menor a la mitad de la cantidad de naranjas,
la mitad de naranjas es menor a dos veces la cantidad de manzanas y dos veces
la cantidad de manzanas es menor o igual a la cantidad de peras al cuadrado.
Restricción: Utilizar comparaciones encadenadas y no utilizar and, or ni not.
"""

bananas = 100
naranjas = 400
manzanas = 300
peras = 30

# COMPLETAR - INICIO

if (bananas < (naranjas / 2) < (manzanas*2) <= (peras**2)):
    comparar_frutas = True

    print(f"La comparación es: {comparar_frutas}")
else:
    comparar_frutas = False
    print(f"La comparación es: {comparar_frutas}")

# COMPLETAR - FIN

assert comparar_frutas

os.system("pause")