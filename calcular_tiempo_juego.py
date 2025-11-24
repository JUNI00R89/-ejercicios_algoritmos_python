

"""
Programa para saber el el tiempo de juego en segundos .
se le solicita al usuario el timepo en horas , minutos 
para saber el tiempo de juego en segundos 

"""


#se le solicita al usuario el tiempo en segundos 

tiempo_segundos = int(input("ingrese el tiempo en segundos:"))

#se le solicita al usuario el tiempo en horas  

tiempo_horas = int(input("ingrese el tiempo en horas:"))

#se le solicita al usuario el tiempo en minutos 

tiempo_minutos  = int(input("ingrese el tiempo en minutos:"))

#se crea la variable que tiene la operacion para saber el tiempo total de juego 

tiempottsegundos = tiempo_horas * 3600 + tiempo_minutos * 60 + tiempo_segundos
 
#se muestra en pantalla el tiempo total de juego 
print("Su tiempo total de juego es de " , ":", tiempottsegundos )

input("PRESIONE ENTER PARA ACABAR")

print("FIN, GRACIAS POR PROBAR")

