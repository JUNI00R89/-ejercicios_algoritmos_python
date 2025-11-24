
"""
Programa para calcular el porcentaje de enemigos derrotados  .
este programa solicita al usuario el total de enemigos y el total de enemigos derrotados 
para saber el porcentaje de ememigos derrotados 

"""








#se le solicita al usuario que ingrese el total de enemigos 
total_enemigos = int(input("INGRESE EL TOTAL DE ENEMIGOS:"))

#se le solicita al usuario que ingrese el total de enemigos derrotados 
enemigos_derrotados = int(input("INGRESE EL TOTAL DE ENEMIGOS DERROTADOS:")) 


#se crea la variable que tiene el proceso para conocer el porcentaje de enemigos 
porcentaje_enemigos = (total_enemigos/enemigos_derrotados)*100

#se muestra en pantalla el porcentaje de enemigos derrotados 
print("EL PORCENTAJE DE ENEMIGOS DERROTADOS ES DE : ", porcentaje_enemigos, "%")