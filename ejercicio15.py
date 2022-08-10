print ('-------------------------')
print ('ejercicio 15: par o impar')
print ('-------------------------')

#entradas 
NUM=int(input('ingrese numero:'))

#proceso
#usando un diccionario
par_impar={
     1:'impar',
     3:'impar',
     5:'impar',
     7:'impar',
     9:'impar',
     2:'par',
     4:'par',
     6:'par',
     8:'par',
     10:'par',
}

print ('\nSALIDA')
print ('-------------------------')
print (par_impar.get(NUM,'numero fuera de rango'))