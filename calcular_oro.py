
"""
Programa para calcular el oro obtenido en 3 niveles .
este programa solicita el oro recojido en cada nivel 
para saber la cantidad de oro recojido en los 3 niveles 

"""








a = input("PRESIONA ENTER PARA INICIAR ")

print(a)





#se le solicita al usuario el oro recolectado en al mision 1 
oro_mision_uno = int(input("ingrese el oro recolectado en la mision 1 :"))

#se le solicita al usuario el oro recolectado en al mision 2
oro_mision_dos = int(input("ingrese el oro recolectado en la mision 2 :"))

#se le solicita al usuario el oro recolectado en al mision 3
oro_mision_tres = int(input("ingrese el oro recolectado en la mision 3 :"))

#se cre la variable de para saber cuanto es el total del oro recolectado 
oro_total = oro_mision_uno + oro_mision_dos + oro_mision_tres


#se muestra el total del oro recolectado 
print ("EL TOTAL DE ORO ES DE :" , oro_total)
                     


b = input("PRESIONA ENTER PARA FINALIZAR")

print (b,"GRACIAS POR PROBAR")