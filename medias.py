"""
Programa que calcula as medias de uma turma de 10 alunos com 5 disciplinas 
"""
import numpy as np

TAMANHO= (2,3)
notas= np.zeros((TAMANHO),dtype= "i")

def media_por_aluno(notas):
    for alunos in range(notas.shape[0]):
        soma= 0
        for disciplinas in range(notas.shape[1]):
            notas[alunos,disciplinas]= int(input(f"Introduza as notas do aluno nº {alunos+1} na {disciplinas+1}º disciplina:"))
            soma= soma + notas[alunos,disciplinas]
        media= soma / notas.shape[1]
        print(f"A media do aluno {alunos+1} foi de {media}")

def media_por_disciplina(notas):
    for disciplinas in range(notas.shape[1]):
        soma= 0
        for alunos in range(notas.shape[0]):
            notas[alunos,disciplinas]= int(input(f"Introduza as notas do aluno nº {alunos+1} na {disciplinas+1}º disciplina:"))
            soma= soma + notas[alunos,disciplinas]
        media= soma / notas.shape[0]
        print(f"A media da disciplina {disciplinas+1} foi de {media}")

media_por_aluno(notas)
media_por_disciplina(notas)