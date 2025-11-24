
"""
Programa para calcular el tiempo de juegos de 3 partidas .
este programa solicita el tiempo de juego de 3 partidas 
para saber el tiempo total de juego 

"""






#se le pide al usuario que ingrese el tiempo de la primera partida 
partida_uno = int(input("INGRESE EL TIEMPO DE PARTIDA 1: "))


#se le pide al usuario que ingrese el tiempo de la segunda partida 
partida_dos= int(input("INGRESE EL TIEMPO DE PARTIDA 2: "))

#se le pide al usuario que ingrese el tiempo de la tercera partida 
partida_tres = int(input("INGRESE EL TIEMPO DE PARTIDA 2: "))

#se crea la variable que tiene el proceso para conocer el promedio de tiempo de partida 
promedio_partida = (partida_uno + partida_dos + partida_tres)/3 

print("EL PROMEDIO DE PARTIDA ES DE :", promedio_partida , "%")
