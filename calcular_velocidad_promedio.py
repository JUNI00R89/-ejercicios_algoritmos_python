
"""
Programa para calcular la velocidad promedio .
este programa solicita la distancia recorrida 
y el tiempo tomado  
para saber la velocidad promedio 

"""



a = input("PRESIONA ENTER PARA INICIAR ")

print(a)

#se le solicita al usuario la distancia recorrida 
distancia_recorrida = float(input("INGRESE LA DISTANCIA RECORRIDA:"))

#se le solicita al usuario el tiempo tomado en recorrer la distancia 
tiempo_tomado = float(input("INGRESE EL TIEMPO TOMADO EN RECORRER LA DISTANCIA :"))

#se cre la variable encargada de la operacion para saber la velocidad 
velocidad_promedio = distancia_recorrida / tiempo_tomado 

#se muestra en pantalla la velocidad promedio  
print("LA VELOCIDAD PROMEDIO ES DE : ", velocidad_promedio ,"/Kh")

b = input("PRESIONA ENTER PARA FINALIZAR")

print (b,"GRACIAS POR PROBAR")