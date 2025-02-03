"""
Programa que lê a matricula de um carro e o tempo que ficou parado no estacionamento
O programa deve ler as matriculas separadas po , e o tempo em (s) separados por ,
CAlcular o caro que ficou mais tempo no estacinomento
"""
import numpy as np
NR_MAX= 3

def ler_dados(matriculas,tempos):
    """
    Função que lê as matriculas e os tempos de estacionamento
    """
    matricula= input("Introduza as matriculas separadas por (,):")
    tempo= input("Introduza os tempos separados por(,):")
    matriculas_separadas= matricula.split(",")
    tempos_separados= tempo.split(",")
    #verificar se as listas têm o mesmo tamanho
    if len(matriculas_separadas) != len(tempos_separados):
        print("O nº de matriculas deve ser igual ao nº de tempos")
        return
    #verificar se o array tem espaço para todos os elementos
    if len(matriculas_separadas ) > NR_MAX:
        print(f"O nº de matriculas deve ser menor que {NR_MAX}")
        return
    for i in range(len(matriculas_separadas)):
        #guardar a matricula
        matriculas[i] = matriculas_separadas[i].strip()
        #guardar os tempos
        tempos[i]= int(tempos_separados[i].strip())

def maior_tempo(matriculas,tempos):
    """
    Função que recebe os tempos e mostra o que mais tempo esteve estacionado
    """
    maior_tempo= 0
    for p in range(NR_MAX):
        if matriculas[p] == "":
            break
        if tempos[p] > tempos[maior_tempo]:
            maior_tempo= p
    print(f"O tempo maior de estacionamento é de {tempos[maior_tempo]} e corresponde a matricula {matriculas[maior_tempo]}")

def mediatempos(tempos):
    """
    Função que recebe os tempos e mostra a media de tempos
    """
    soma= 0
    preenchidos = 0
    for p in range(len(tempos)):
        if tempos[p] == 0:
            break
        soma = soma + tempos[p]
        preenchidos= preenchidos + 1
    media= soma /preenchidos
    print(media)

def maior_que_media(matriculas,tempos):
    """
    Função que recebe os tempos e mostra os tempos que são maiores do que a media
    """
    media= mediatempos(tempos)
    for i in range (NR_MAX):
        if tempos[i] == 0:
            break
        if tempos[i] > media:
            print(f"{matriculas[i]} este {tempos[i]} que é superior a média")

def matricula_repetida(matriculas):
    """
    Funão que recebe as matriculas e verifica se existem matriculas repetidas
    """
    for i in range (matriculas):
        contar = 0
        if i == "":
            break
        for j in range(matriculas):
                contar = contar + 1
        if contar > 1:
            print(f"A matricula {matriculas[i]} esteve estacionada {contar} vezes")

def menu():
    """
    Apresenta um menu de opções para gerenciar as matrículas de veículos e tempos de estacionamento.
    As opções disponíveis permitem ler dados de matrículas, consultar o tempo de estacionamento mais longo, 
    calcular a média dos tempos de estacionamento e listar matrículas com tempos superiores à média.
    """
    op= 0
    matriculas= np.empty(NR_MAX,dtype= "U8")
    tempo= np.empty(NR_MAX)
    while op != 6:
        op= input("1.Ler matricula\n2.Consultar tempos\n3.Media de tempos\n4.Melhor tempo\n5.Matricula repetida\n")
        if op == "1":
            ler_dados(matriculas,tempo)
        elif op == "2":
            maior_tempo(matriculas,tempo)
        elif op == "3":
            mediatempos(tempo)
        elif op == "4":
            maior_que_media(matriculas,tempo)
        elif op == "5":
            matricula_repetida(matriculas)
        
def main():
    menu()

if __name__ == "__main__":
    main()