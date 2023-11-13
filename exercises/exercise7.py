import os

""""Tuplas y Desempaquetado"""


"""
A partir de ls siguiente lista instanciar una tupla que contenga todos sus valores
y en el mismo orden.
"""

lista = ["casa", "perro", "pato", "gato"]

# COMPLETAR - INICIO

tupla = tuple(lista)

print(f"{tupla}")

# COMPLETAR - FIN

assert tupla == ("casa", "perro", "pato", "gato")

os.system("pause")


"""
A partir de ls siguiente tupla instanciar una lista que contenga todos sus valores
y en el mismo orden.
"""

tupla = "casa", "perro", "pato", "gato", "tenedor"



# COMPLETAR - INICIO

lista = list(tupla)


print(f"{lista}")

# COMPLETAR - FIN

assert lista == ["casa", "perro", "pato", "gato", "tenedor"]

os.system("pause")


"""
Desempaquetar la siguiente tupla en las variables a, b y c
"""

tupla = ("primer", 25, [1, 2, 3])


# COMPLETAR - INICIO

a,b,c = tupla

print(f"{a}, {b}, {c}")

# COMPLETAR - FIN

assert a == "primer" and b == 25 and c == [1, 2, 3]

os.system("pause")


"""
Desempaquetar la siguiente tupla y luego sumar sus valores
"""

tupla = (87, 98, 35, 67, 4, 9)

# COMPLETAR - INICIO

nro_1, nro_2, nro_3, nro_4, nro_5, nro_6 = tupla

total = nro_1 + nro_2 + nro_3 + nro_4 + nro_5 + nro_6

print(f"{total}")

# COMPLETAR - FIN

assert total == 300

os.system("pause")

"""
Desempaquetar la siguiente lista y luego concatenar sus elementos
Restricción: Utilizar f-Strings.
"""

lista = ["esta", "mañana", "sali", "a", "correr"]

# COMPLETAR - INICIO

a,b,c,d,e = lista

string_concatenado = f"{a} {b} {c} {d} {e}"

print(f"{string_concatenado}")


# COMPLETAR - FIN

assert string_concatenado == "esta mañana sali a correr"

os.system("pause")

"""
Desempaquetar el primer elemento de la siguiente tupla
Restricción: Utilizar desempaquetado con comodines
"""

tupla = (73, 45, 344, 3434, 2)

# COMPLETAR - INICIO

primer, *rest = tupla

print(f"{primer}")

# COMPLETAR - FIN

assert primer == 73

os.system("pause")


"""
Desempaquetar el primer y el último elemento de la siguiente lista y luego sumarlos
Restricción: Utilizar desempaquetado con comodines
"""

lista = [73, 45, 344, 3434, 2]

# COMPLETAR - INICIO

primer_nro, *rest, ultimo_nro = lista

suma = primer_nro + ultimo_nro

print(f"{suma}")

# COMPLETAR - FIN

assert suma == 75

os.system("pause")


"""
Desempaquetar el primer, el segundo, el tercer, el cuarto y el quinto elemento de la
siguiente tupla y luego concatenarlos
Restricción: Utilizar desempaquetado con comodines y f-Strings
"""

tupla = ("anoche", "fui", "a", "la", "fiesta", "pero", "no", "pude", "entrar")

# COMPLETAR - INICIO

a, b, c, d, e, *rest = tupla

string_concatenado = f"{a} {b} {c} {d} {e}"

print(f"{string_concatenado}")

# COMPLETAR - FIN

assert string_concatenado == "anoche fui a la fiesta"

os.system("pause")