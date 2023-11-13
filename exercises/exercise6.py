import os

"""Listas"""

"""
Inicializar una lista vacía y luego agregarle 4 elementos cualquiera
Restricción: Utilizar el método append
"""

# COMPLETAR - INICIO
lista_01 = []

lista_01.append("Hola")
lista_01.append(" como")
lista_01.append(" estás")
lista_01.append("?")

print(f"{lista_01[0]}{lista_01[1]}{lista_01[2]}{lista_01[3]}")


# COMPLETAR - FIN

assert len(lista_01) == 4

os.system("pause")

"""
Extraer el cuarto elemento de la lista
Restricción: Utilizar el método pop
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]

# COMPLETAR - INICIO

elemento_extraido = lista.pop(3)

print(f"El elemento eliminado de la lista es: {elemento_extraido}")

# COMPLETAR - FIN

assert elemento_extraido == 6

os.system("pause")


"""
Concatenar las siguientes listas
Restricción: Utilizar el método extend
"""

lista_a = [1, 2, 3]
lista_b = ["4", "5", "6"]
lista_c = ["siete", "ocho", "nueve"]

# COMPLETAR - INICIO

lista_a.extend(lista_b)
lista_a.extend(lista_c)
listas_concatenadas_01 = lista_a

print(f"{listas_concatenadas_01}")

# COMPLETAR - FIN

assert listas_concatenadas_01 == [1, 2, 3, "4", "5", "6", "siete", "ocho", "nueve"]

os.system("pause")


"""
Agregar la variable variable_01 en la tercer posición de la lista lista_nueva
Restricción: Utilizar el método insert
"""

variable_01 = 2
lista_nueva = [0, 1, 3, 4]

lista_nueva.insert(2, variable_01)

# COMPLETAR - INICIO

print(f"{lista_nueva}")

# COMPLETAR - FIN

assert lista_nueva == [0, 1, 2, 3, 4]

os.system("pause")


"""
Armar una lista que contenga el primer y el último elemento de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, 42, 81, 6, "la"]

primer_elemento = lista[0]
ultimo_elemento = lista[5]

lista_primero_y_ultimo = []

lista_primero_y_ultimo.append(primer_elemento)
lista_primero_y_ultimo.append(ultimo_elemento)



# COMPLETAR - INICIO

print(f"{lista_primero_y_ultimo}")

# COMPLETAR - FIN

assert lista_primero_y_ultimo == ["ho", "la"]

os.system("pause")


"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

primer_elemento = lista[0]
segundo_elemento = lista[1]
tercer_elemento = lista[2]

lista_primeros = []

lista_primeros.append(primer_elemento)
lista_primeros.append(segundo_elemento)
lista_primeros.append(tercer_elemento)



# COMPLETAR - INICIO

print(f"Método append junto al indexado simple: {lista_primeros}")

# COMPLETAR - FIN

assert lista_primeros == ["ho", 3.1416, "la"]

os.system("pause")


"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar indexado múltiple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

lista_primeros = lista[:3]

# COMPLETAR - INICIO

print(f"Indexado multiple: {lista_primeros}")

# COMPLETAR - FIN

assert lista_primeros == ["ho", 3.1416, "la"]

os.system("pause")


"""
Armar una lista que contenga los primeros 2 y los últimos 2 elementos de la
siguiente lista
Restricción: Utilizar el método extend junto al indexado múltiple
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]

# COMPLETAR - INICIO

lista_primeros_y_ultimos = []
lista_primeros_y_ultimos.extend(lista[:2])
lista_primeros_y_ultimos.extend(lista[-2:])

print(f"Método extend junto al indexado múltiple: {lista_primero_y_ultimo}")

# COMPLETAR - FIN

assert lista_primeros_y_ultimos == ["ho", "la", "como", "estas?"]

os.system("pause")


"""
Concatenar las siguientes 2 listas
Restricción: Utiliar el operador +
"""

lista_01 = [0, 1, 2, 3]
lista_02 = [5, 6]

lista_concatenada = lista_01 + lista_02

# COMPLETAR - INICIO

print(f"Concatenar las siguientes 2 listas, utiliar el operador +: {lista_concatenada}")

# COMPLETAR - FIN

assert lista_concatenada == [0, 1, 2, 3, 5, 6]

os.system("pause")


"""
Concatenar 3 veces la siguiente lisa consigo misma
Restricción: Utiliar el operador *
"""

lista_01 = [0, 1, 0, 1, 0, 1]

lista_duplicada = lista_01 * 3

# COMPLETAR - INICIO

print(f"Concatenar 3 veces la siguiente lisa consigo misma, utiliar el operador *: {lista_duplicada}")


# COMPLETAR - FIN

assert lista_duplicada == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

os.system("pause")


"""
Verificar si el siguiente elemento pertenece a la lista
Restricción: Utiliar el operador in
"""

elemento = 1.0
lista = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1.0, 1, 0, 1, 0, 1]

# COMPLETAR - INICIO

variable_booleana = elemento in lista

print(f"Utiliar el operador in: {variable_booleana}")

# COMPLETAR - FIN

assert variable_booleana

os.system("pause")


"""
Verificar si las siguientes listas son iguales
Restricción: Utilizar el operador ==
"""

lista_01 = [1, 2, 3, 4.5, 6, 7]
lista_02 = [1, 3, 2, 4, 5, 6, 7]

# COMPLETAR - INICIO

son_iguales = lista_01 == lista_02

print(f"Las siguientes listas son iguales: {son_iguales}")


# COMPLETAR - FIN

assert not son_iguales

os.system("pause")


"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno no tiene examenes aprobados.
Restricción: Utilizar el método any
"""

notas = [False, False, False, False, False, False, False, False, False]

# COMPLETAR - INICIO

no_tiene_examenes_aprobados = any(notas)

print(f"{no_tiene_examenes_aprobados}")

# COMPLETAR - FIN

assert no_tiene_examenes_aprobados

os.system("pause")


"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno ha aprobado todos sus exámenes.
Restricción: Utilizar el método all
"""

notas = [True, True, False, True, True, True, True, True, True, True, True, True]

# COMPLETAR - INICIO

tiene_todo_aprobado = all(notas)

print(f"{tiene_todo_aprobado}")

# COMPLETAR - FIN

assert not tiene_todo_aprobado

os.system("pause")