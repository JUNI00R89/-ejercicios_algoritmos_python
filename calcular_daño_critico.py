
"""
Programa para calcular el costo total de 3 mejoras .
este programa solicita el costo de las 3 mejoras 
para saber el costo de las 3 mejoras juntas

"""


a = input("PRESIONA ENTER PARA INICIAR ")

print(a)


#SE LE PIDE AL USUARIO EL DAÑO BASE DEL ATAQUE 
daño_base = float(input("INGRESE EL DAÑO BASE:"))

#SE LE PIDE AL USUARIO EL MULTIPLICADOR DE DAÑO 
multiplicador_critico = float(input("INGRESA MULTIPLICADOR CRITICO:"))


#SE CREA LA VARIABLE DONDE ESTA LA OPERACION PARA CONOCER EL DAÑO CRITICO
daño_critico =  daño_base * multiplicador_critico 

#SE MUESTRA EN PANTALLA EL DAÑO CRITIVO 
print( "SU DAÑO CRITICO ES DE :" , daño_critico) 
