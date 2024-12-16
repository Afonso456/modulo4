import numpy #or import numpy as np

numeros= numpy.array([10,14,-5,33,120])

for i in range(5):
    numeros[i] =0

array_0d= numpy.array(40) #array de zero dimensões 

print(type(numeros))
print(type(array_0d))
print(array_0d)

print(numeros.ndim) # numero de dimensões que o array possui

for i in range(5):
    print(numeros[i])

for x in numeros:
    print(x)

#for x in (len(numeros)):
#    print(numeros[x])

#criar array vazio
vazio= numpy.empty(10)
print(vazio)

#criar um array com zeros
zeros= numpy.zeros(10)
print(zeros)