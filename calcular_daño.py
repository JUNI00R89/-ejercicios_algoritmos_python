
"""
Programa para calcular el daño de 3 ataques.
este programa solicita el daño de las 3 ataques 
para saber el costo de las 3 ataques  juntos 

"""








#se solicita el daño del primer ataque al usuario 
daño_ataque_uno = float(input("'Ingrese el daño del primer ataque:'"))

#se solicita el daño del segundo ataque al usuario 
daño_ataque_dos = float(input("'Ingrese el daño del segundo ataque:'"))

#se solicita el daño del tercer ataque al usuario 
daño_ataque_tres= float(input("'Ingrese el daño del tercer ataque:'"))

#se crea la variable de daño total que tiene la operacion para saber todo el daño total 
daño_total = daño_ataque_uno + daño_ataque_dos + daño_ataque_tres
  

print("'el daño total es de' : ",  daño_total )
