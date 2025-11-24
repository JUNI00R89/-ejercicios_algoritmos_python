
"""
Programa para calcular el tiempo restante de la mision  .
este programa solicita el tiempo total y el tiempo transcurrido 
para saber el tiempo restante 

"""


#se le solicita al usuario el timepo total de la mision 
tiempo_total_mision = int(input("INGRESE EL TIEMPO TOTAL DE LA MISION:"))

#se le pide al usuario el tiempo transcurrido en la mision 
tiempo_transcurrido = int(input("INGRESE EL TIEMPO TRANSCURRIDO:"))

#se crea la variable para conocer el tiempo restante 
tiempo_restante = tiempo_total_mision - tiempo_transcurrido 

minutos = tiempo_restante // 60

segundos = tiempo_restante % 60 



#se muestra en pantalla el tiempo restante en minutos y segundos 
print(tiempo_restante,":" ,minutos,"m",":" , segundos ,"s")
