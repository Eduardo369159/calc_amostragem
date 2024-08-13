from main import Calculos
import os

cl = Calculos()
sair = 0
while sair == 0:
    os.system('cls')
    print("+-------------------------------------------------------+")
    print("|                   CÁLCULO DE AMOSTRA                  |")
    print("|                                                       |")
    print("|           _____          _                            |")
    print("|          |  ___| ______ | |__  _____    ____          |")
    print("|          | |_   |____  ||  __|/  __ \ /  __ |         |")
    print("|          |  _/  /      || |  |   ___/|  |             |")
    print("|          | |   |  (_|  || |_ |  \___ |  |__           |")
    print("|          \_|    \___;__|\___| \_____| \ ____|         |")
    print("|                                                       |")
    print("+-------------------------------------------------------+")
    print('ESCOLHA O MODELO DE CALCULO')
    print('=====================================')
    print('1° - Aleatória Simples')
    print()
    print('2° - Estratificada Proporcional')
    print()
    print('3° - Sistematica')
    print('=====================================')
    print('Digite a opção desejada')
    escolha1 = int(input('(1, 2 ou 3):'))
    if escolha1 == 1:
        os.system('cls')
        print('MODELO ALEATORIO SIMPLES')
        print('=====================================')
        print('Escreva o tamanho da sua população total')
        N = int(input('_:'))
        print('Escreva o percentual de erro tolerado')
        n0 = int(input('(5, 4..., 1):'))
        if n0 == 5:
            n0 = 400
        elif n0 == 4:
            n0 = 625
        elif n0 == 3:
            n0 = 1111
        elif n0 == 2:
            n0 = 2500
        elif n0 == 1:
            n0 = 10000
        os.system('cls')
        print(cl.aleatoria_simples(N, n0))
        print()
        print('=====================================')
        print('Deseja sair?')
        escolha_s = int(input('(1 - Sim, 2 - Não :)'))
        if escolha_s == 2:
            pass
        else:
            os.system('cls')
            sair = 1
    if escolha1 == 2:
        os.system('cls')
        print('MODELO ESTRATIFICADO PROPORCIONAL')
        print('=====================================')
        print('Escreva o tamanho da sua população total')
        N = int(input('_:'))
        print('Escreva o percentual de erro tolerado')
        n0 = int(input('(5, 4..., 1):'))
        if n0 == 5:
            n0 = 400
        elif n0 == 4:
            n0 = 625
        elif n0 == 3:
            n0 = 1111
        elif n0 == 2:
            n0 = 2500
        elif n0 == 1:
            n0 = 10000
        print('Escreva a quantidade de grupos que deseja dividir sua população')
        grupo = int(input('_:'))
        os.system('cls')
        carga = cl.estratificada_proporcional(grupo, N, n0)
        for i in carga:
            print(i)
        print()
        print('=====================================')
        print('Deseja sair?')
        escolha_s = int(input('(1 - Sim, 2 - Não :)'))
        if escolha_s == 2:
            pass
        else:
            os.system('cls')
            sair = 1
    if escolha1 == 3:
        os.system('cls')
        print('MODELO SISTEMATICO')
        print('=====================================')
        print('Escreva o tamanho da sua população total')
        N = int(input('_:'))
        print('Escreva o percentual de erro tolerado')
        n0 = int(input('(5, 4..., 1):'))
        if n0 == 5:
            n0 = 400
        elif n0 == 4:
            n0 = 625
        elif n0 == 3:
            n0 = 1111
        elif n0 == 2:
            n0 = 2500
        elif n0 == 1:
            n0 = 10000
        os.system('cls')
        print(cl.sistematica(N, n0))
        print()
        print('=====================================')
        print('Deseja sair?')
        escolha_s = int(input('(1 - Sim, 2 - Não :)'))
        if escolha_s == 2:
            pass
        else:
            os.system('cls')
            sair = 1


