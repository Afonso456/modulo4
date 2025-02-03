import numpy as np
array= np.array([1,2,3])
def soma(array):
    soma_valores= 0
    for i in array:
        soma_valores += i
    return soma_valores
    
print(soma(array))