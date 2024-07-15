import itertools
import pyautogui as pg
from time import sleep as sl
import random 

A1=(2433,436)
A2=(2433,563)
A3=(2433,686)
A4=(2433,813)
A5=(2433,933)
B1=(2556,425)
B2=(2556,556)
B3=(2556,678)
B4=(2556,810)
B5=(2556,928)
C1=(2678,430)
C2=(2678,555)
C3=(2678,683)
C4=(2678,810)
C5=(2678,930)
D1=(2802,430)
D2=(2802,553)
D3=(2802,684)
D4=(2802,806)
D5=(2802,929)
E1=(2929,433)
E2=(2929,559)
E3=(2929,685)
E4=(2929,805)
E5=(2929,928)
jogarSacar=(3326,635)
CoordeNadasAtivas = [A1,A2,A3,A4,A5,B1,B2,B3,B4,B5,C1,C2,C3,C4,C5,D1,D2,D3,D4,D5,E1,E2,E3,E4,E5]
#######################CÓDIGO###########################
# Definir caracteres possíveis para geração de senha
caracteres = CoordeNadasAtivas

# Quantas vezes as senhas geradas deverão ser apresentadas
qtd_repeticoes = 1

# Lista que irá armazenar as senhas
bd = list()
tempoTransicao = 1.5
tempoRestart = 2.5

def MovimentosFalsos():
    # a = random.choice(CoordeNadasAtivas)
    # b = random.choice(CoordeNadasAtivas)
    # c = random.choice(CoordeNadasAtivas)
    d = random.choice(CoordeNadasAtivas)
    # e = random.choice(CoordeNadasAtivas)
    # f = random.choice(CoordeNadasAtivas)
    # g = random.choice(CoordeNadasAtivas)
    # h = random.choice(CoordeNadasAtivas)
    # pg.moveTo(a)
    # pg.moveTo(b)
    # pg.moveTo(c)
    pg.moveTo(d)
    # pg.moveTo(e)

# execucoes = int(input('Quantas Excecuções deseja Realizar?\n'))
# banca = input("informe o valor do saldo da sua banca:\n")
# conta = execucoes #contagem regressiva
# # Gerador de combinações possíveis de caracteres
# for tamanho in range(qtd_repeticoes): #define a quantidade de repetições
# 	#Define a quantidade de caracteres terá a senha gerada
#     # print(jogarSacar[0],jogarSacar[1],A1[0],A1[1])
#     print(sl(tempoRestart))
    
    # print(a,b,c,d,e)
    # for tentativa in itertools.product(random.choice(caracteres), repeat=5): 
    # for exect in range(execucoes): 
    #     a = random.choice(CoordeNadasAtivas)
    #     b = random.choice(CoordeNadasAtivas)
    #     c = random.choice(CoordeNadasAtivas)
    #     d = random.choice(CoordeNadasAtivas)
    #     e = random.choice(CoordeNadasAtivas)
    #     f = random.choice(CoordeNadasAtivas)
    #     g = random.choice(CoordeNadasAtivas)
    #     h = random.choice(CoordeNadasAtivas)
    #     # senha = tentativa
    #     # Lógica para elinar sequencias repetidas como 111,222,333,aaa,bbb...
    #     # A quantidade comparativa deve seguir o número de reapet='?' da terceira linha acima
    #     # if not senha[0] == senha[1] == senha[2]== senha[3] == senha[4]:
    #     if not a == b == c == d == e == f == g == h:    
#         #if not a or b or c or d or e or f or g or h in xy:
#             print('ok')
#             pg.click(jogarSacar[0], jogarSacar[1]) #Iniciar o Jogo
#             # a, b, c, d, e = senha[0],senha[1],senha[2],senha[3],senha[4]
#             sl(5)
#             for z in range(2):
#                 MovimentosFalsos()
#             pg.click(a)
#             sl(tempoTransicao)
#             # for z in range(10):
#             #     MovimentosFalsos()
#             pg.click(b)
#             sl(tempoTransicao)
#             # for z in range(11):
#             #     MovimentosFalsos()
#             pg.click(c)
#             sl(tempoTransicao)
#             # for z in range(3):
#             #     MovimentosFalsos()
#             # pg.click(d)
#             # sl(tempoTransicao)
#             # # for z in range(2):
#             # #     MovimentosFalsos()
#             # pg.click(e)
#             # sl(tempoTransicao)
#             # # for z in range(7):
#             # #     MovimentosFalsos()
#             # pg.click(f)
#             # sl(tempoTransicao)
#             # # for z in range(5):
#             # #     MovimentosFalsos()
#             # pg.click(g)
#             # sl(tempoTransicao)
#             # # for z in range(4):
#             # #     MovimentosFalsos()
#             # pg.click(h)
#             # sl(tempoTransicao)
#             pg.click(x=jogarSacar[0],y=jogarSacar[1]) #sacar o valor
#             conta=conta-1
#             print("Execuções restantes:",conta)
            
#             sl(tempoRestart)
#     print('Este foi o valor inicial da sua Banca:',banca)
            

# #######################CÓDIGO###########################

        
# # 
# # while True:
#     # print(pg.position())

    
    

    
    