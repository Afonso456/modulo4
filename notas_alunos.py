import numpy as np

NR_ALUNOS= 10

#definir o array
notas= np.zeros(NR_ALUNOS)
soma=0
for n in range (NR_ALUNOS):
    notas[n] = float(input(f"Introduza a nota do aluno nº {n+1}:"))
    soma= soma + notas[n]
media= soma / NR_ALUNOS
print(f"A media das notas foi de {media}")

#listar as notas que são superiores a media

for n in range(NR_ALUNOS):
    if notas[n] > media:
        print(f"A nota {notas[n]} do aluno {n+1} é superior a media ")