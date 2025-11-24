"""
Programa para calcular los minutos restantes  .
este programa solicita al usuario el tiempo en minutos  
para tambien conocer el tiempo en horas y ver los minutos y horas restantes 

"""
a = input("PRESIONA ENTER PARA INICIAR")

print(a)


#se le solicita el usuario que ingrese el tiempo en minutos 
tiempo_minutos = int(input("INGRESE EL TIEMPO EN MINUTOS:"))

#se crea la variable para convertir los minutos en horas 
tiempo_horas =  tiempo_minutos // 60 

#se crea la variable para conocer los minutos restantes 
minutos_restantes = tiempo_minutos % 60 


#se muestra en pantalla el tiempo en minutos y en horas 
print(f"el tiempo es de " ,tiempo_horas, "horas", minutos_restantes, "minutos ")


