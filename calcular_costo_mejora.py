
"""
Programa para calcular el costo total de 3 mejoras .
este programa solicita el costo de las 3 mejoras 
para saber el costo de las 3 mejoras juntas

"""




bienvenida = input("QUIERES CONOCER EL COSTO TOTAL DE LAS MEJORAS? PRESIONA ENTER Y EMPIEZA ")

print(bienvenida)

#se le pide al usuario el costo de la mejora 1 
costo_mejora_uno = int(input("INGRESE EL COSTO DE LA MEJORA 1 : "))

#se le pide al usuario el costo de la mejora 2
costo_mejora_dos = int(input("INGRESE EL COSTO DE LA MEJORA 2 : "))

#se le pide al usuario el costo de la mejora 3
costo_mejora_tres = int(input("INGRESE EL COSTO DE LA MEJORA 3 : "))

#se crea la variable para conocer el costo total de las 3 mejoras 
costo_total = costo_mejora_uno + costo_mejora_dos + costo_mejora_tres 

print("EL COSTO DE LAS 3 MEJORAS ES DE  " , "$" , costo_total)