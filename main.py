import os
import random as rn

class Calculos():
    def aleatoria_simples(self, N,n0):
        n = int((N*n0)/(N+n0))
        return(f'A sua amostra deve possuir {n} ocorrências, contendo {round((n/N)*100,2)}% da população')
    
    def estratificada_proporcional(self, grupos, N, n0):
        n = int((N*n0)/(N+n0))
        percent = float(n/N)
        verificar_populacao = 0
        qtd_grupo = []
        for i in range(grupos):
            populacao = int(input(f'Escreva a população para o grupo {i+1}: '))
            verificar_populacao+=populacao
            qtd_grupo.append(int(populacao*percent))
        while verificar_populacao != N:
            os.system('cls')
            print('A população informada é diferente da população total da sua base, verifique seus dados')
            break
        index = 1
        os.system('cls')
        for i in qtd_grupo:
            yield(f'Amostra grupo{index}: {i} - com {percent*100}% da população')
            index+=1

    def sistematica(self, N, n0):
        n = int((N*n0)/(N+n0))
        sistema = int(N/n)
        sec = []
        primario = rn.randint(1,n)
        sec.append(primario)
        for i in range(sistema-2):
            sec.append(sec[i]+n)
        sec.append(N-n+primario)
        os.system('cls')
        return(sec)




