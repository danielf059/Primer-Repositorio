#EJERCICIO 1
alumnos_clase = ["Maria","Jose","Carlos","Martina","Isabel","Tomas", "Daniela"]

for alumno in alumnos_clase:
    print(f"Hola {alumno}")
    


#EJERCICIO 2
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
print(f"La suma de todos los numeros es: {suma_numeros}")



#ejercicio 3
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0


for num in lista_numeros:
    if num % 2 == 0:
        suma_pares = suma_pares + num
    elif num % 2 == 1:
        suma_impares = suma_impares + num
print(f"La suma de los numeros pares es: {suma_pares}")
print(f"La suma de los numeros impares es: {suma_impares}")