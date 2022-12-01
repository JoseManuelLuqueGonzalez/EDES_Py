"""
1.	Implementa dos funciones para obtener la parte entera y la parte decimal de un 
número en punto flotante (double). La definición de las funciones es como sigue: 
•	def get_parte_entera(numero) return parte entera del numero
•	def get_parte_decimal(numero) return parte decimal del numero 
"""

def get_parte_entera(numero):
    st_numero = str(numero)
    arr_numero = st_numero.split(".")
    return int(arr_numero[0])

def get_parte_decimal(numero):
    st_numero = str(numero)
    arr_numero = st_numero.split(".")
    return int(arr_numero[1])
