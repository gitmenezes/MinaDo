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

# Definir caracteres possíveis para geração de senha
caracteres = CoordeNadasAtivas

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

repet = int(input('Informe quantas apostas deseja Realizar?\n'))
locMinas = int(input('Quantos diamantes quer encontra por aposta?\n'))
banca = input('Informe o valor que possui em dinheiro em sua banca:\n')
# conta = repet

def autoPlayer():
    for x in range(repet): #Quantidade de apostas que serão realizadas
        print('Apostas: ',x+1, 'de: ',repet)
        sl(3)
        pg.click(x=jogarSacar[0],y=jogarSacar[1]) #sacar o valor
        sl(3)
        for x in range(locMinas): #Quantidade de Diamantes que serão resgatados
            escolha = random.choice(CoordeNadasAtivas)
            pg.click(escolha)
            sl(4)
        pg.click(x=jogarSacar[0],y=jogarSacar[1]) #sacar o valor
                
autoPlayer() #executar o código