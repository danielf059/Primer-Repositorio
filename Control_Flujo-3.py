#EJERCICIO 3
habla_ingles = True
sabe_python = False

if (habla_ingles == True) and (sabe_python == True):
    print("Cumple con los requisitos para postularse")
    
elif (habla_ingles == False) and (sabe_python == True):
    print("Para postularse, necesita tener conocimientos en inglés")
    
elif (habla_ingles == True) and (sabe_python == False):
    print("Para postularse, necesita saber programar en Python")
    
else:
    print("Para postularse, necesita saber programar en Python y tener conocimientos en inglés")