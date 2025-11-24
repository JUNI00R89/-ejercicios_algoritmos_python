
"""
Programa para calcular el promedio de un equipo .
este programa solicita el nivel de los 3 jugadores 
para saber promedio del equipo 

"""


b = input("PRESIONA ENTER PARA EMPEZAR" )


print(b)


#se le pide al usuario que digite el nivel del primer jugador 
jugador_uno = float(input("INSERTE EL NIVEL DE JUGADOR 1:"))

#se le pide al usuario que digite el nivel del segundo  jugador 
jugador_dos = float(input("INSERTE EL NIVEL DE JUGADOR 2:"))


#se le pide al usuario que digite el nivel del tercer jugador 
jugador_tres = float(input("INSERTE EL NIVEL DE JUGADOR 3:"))

#se crea la variable donde esta la operacion para saber el nivel de los 3 jugadores 
nivel_jugadores = jugador_uno + jugador_dos + jugador_tres 

#se muestra en pantalla el nivel de los 3 jugadores 
print("EL NIVEL DE LOS 3 JUGADORES  DE : " , nivel_jugadores )


a = input("CONOCE EL PROMEDIO DEL EQUIPO PRESIONANDO ENTER")



#se crea la variable para saber el promedio del equipo 
nivel_promedio_equipo = nivel_jugadores / 3 

#se muestra en pantalla el promedio del equipo 
print( "ESTE EL PROMEDIO DEL EQUIPO" , nivel_promedio_equipo)


