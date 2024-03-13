#Primer ejercicio
operacion = float((3 + 2) /2.5 ) **2
print(operacion)

#Segundo ejercicio
payasos = (112*23)
muñecas = (75*54)
peso_total = payasos + muñecas

print(f"El peso total en gramos es: {peso_total}")

#Tercer ejercicio
cadena = "Te quiero solo como amigo"
print(f"Los dos primeros caracteres son: {cadena [0:2]}")
print(f"Los tres ultimos caracteres son: {cadena[-3:]}")
print(f"Cada dos caracteres: {cadena[::2]}")
print(f"Sentido inverso: {cadena[::-1]}")
print(f"Sentido normal e inverso: {cadena[0:]} {cadena[::-1]}")

#Cuarto ejercicio
cadena = "Separado" 
separar_con_comas =","                        
cadena_con_comas = cadena.replace("",separar_con_comas)  [1:-1]
print(cadena_con_comas)




