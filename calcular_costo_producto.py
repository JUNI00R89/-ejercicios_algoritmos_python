
"""
Programa para calcular el costo total de 3 productos  .
este programa solicita el costo de las 3 productos  
para saber el costo de las 3 productos juntos 

"""






a= input("PRESIONA ENTER PARA INICIAR ")
print ( a )

#se le pide al usuario el costo de primer producto 
producto_uno = int(input("INGRESE EL COSTO DEL PRODUCTO 1: "))

#se le pide al usuario el costo de segundo  producto 
producto_dos  = int(input("INGRESE EL COSTO DEL PRODUCTO 2: "))

#se le pide al usuario el costo del tercer  producto 
producto_tres = int(input("INGRESE EL COSTO DEL PRODUCTO 3: "))

#se crea la variable que tiene la operacion para conocer el costo final de los 3 productos 
costo_final = producto_uno + producto_dos + producto_tres 

#se muestra en pantalla el costo final de los 3 productos 
print("EL COSTO DE LOS 3 PRODUCTOS ES DE ", costo_final ,"$", "TENGA BUEN DIA")
