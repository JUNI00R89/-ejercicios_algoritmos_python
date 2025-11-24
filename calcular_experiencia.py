
"""
Programa para calcular la experiencia obtenida en 3 niveles  .
este programa solicita al usuario la experiencia obtenida en cada nivel 
para saber  cuanta experiencia obtuvo en las misiones

"""


#se solicita al usuario la experiencia ganada en la primera mision 
experiencia_mision_uno = float(input("Ingrese la  experiencia ganada en la mision 1:"))

#se solicita al usuario la experiencia ganada en la segunda  mision 
experiencia_mision_dos = float(input("Ingrese la experiencia ganada en la mision 2:"))

#se solicita al usuario la experiencia ganada en la tercera  mision 
experiencia_mision_tres = float(input("Ingrese  la experiencia ganada en la mision 3:"))

#se crea la variable que tiene los procesos para descubrir la experiencia total 
experiencia_total = experiencia_mision_uno + experiencia_mision_dos + experiencia_mision_tres

#se muestra en pantalla la experiencia total 
print ("!la experiencia total ganada es de¡:" , experiencia_total)

