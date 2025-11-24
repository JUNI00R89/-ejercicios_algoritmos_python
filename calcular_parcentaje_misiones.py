
"""
Programa para calcular el porcentaje de misiones completadas.
este programa solicita el total de misiones y las misiones completadas 
para saber el porcentaje de misiones completadas 

"""








a = input("PRESIONA ENTER PARA EMPEZAR 😀")

print(a)


#se le pide al usuario la cantidad de misiones 
total_misiones = int(input("INGRESE EL TOTAL DE MISIONES:"))

#se le pide al usuario las misiones completadas
misiones_completada = int(input("INGRESE EL TOTAL DE MISIONES COMPLETADAS:")) 
 
 #se crea la variable que tiene la operacion para saber el porcentaje 
porcentaje_misiones = (misiones_completada/total_misiones)*100

#se muestra en pantalla el porcentaje de misiones completadas 
print("EL PORCENTAJE DE MISIONES COMPLETADA ES DE ",porcentaje_misiones,"%")

