


# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:32:38 2020

@author: bru_b
"""


#Inicio do Jogo
print('Bem vindo(a) ao Kassinão!')
print('Já que é a sua primeira vez toma aí 1000 fichas')
print('Bora jogar Craps')

#Variaveis
ficha=1000
Pass_Line_Bet=False
Field=False
Any_Craps=False
Twelve=False
Point=False
aposta1=0
aposta2=0
aposta3=0
aposta4=0
#Rolada de dados
from random import randint
dado1=(randint(1,6))
dado2=(randint(1,6)) 
dados=dado1+dado2

#Resposta do user
resposta=input('Você vai querer jogar?(s/n):')
if resposta=='s':
    print('Agora estamos no Come Out. Você pode fazer as seguintes apostas: Pass_Line_Bet, Field, Any_Craps, Twelve.')
    resposta=input('Você deseja fazer uma Pass Line Bet:(s/n):')
    if resposta=='s':
        Pass_Line_Bet=True
        aposta1=int(input('Quanto você vai apostar?'))
        ficha=ficha-aposta1
    else:
        None
    resposta=input('Você deseja fazer uma Field:(s/n):')
    if resposta=='s':
        Field=True
        aposta2=int(input('Quanto você vai apostar?'))
        ficha=ficha-aposta2    
    else:
        None
    resposta=input('Você deseja fazer uma Any Craps:(s/n):')
    if resposta=='s':
        Any_Craps=True
        aposta3=int(input('Quanto você vai apostar?'))
        ficha=ficha-aposta3
    else:
        None
    resposta=input('Você deseja fazer uma Twelve:(s/n):')
    if resposta=='s':
        Twelve=True
        aposta4=int(input('Quanto você vai apostar?'))
        ficha=ficha-aposta4
    else:
        None
else:
    print('Até a próxima!')
    ficha=0  
#Aposta Pass Line Bet
while not ficha==0:
    if Pass_Line_Bet:
        if dados==7 or dados==11:
            ficha=ficha+aposta1*2
            print('Parabéns você ganhou Pass Line Bet, agora você tem {} fichas.'.format(ficha))
            Pass_Line_Bet=False
        elif dados==2 or dados==3 or dados==12:
            print('Infelizmente você perdeu, agora você tem {} fichas'.format(ficha))
            Pass_Line_Bet=False
        else:
            print('Saiu {0} nos dados agora estamos entrendo na faze de Point'.format(dados))
            Pass_Line_Bet=False
            Point=True
#Aposta Field
    if Field:
        if dados==5 or dados==6 or dados==7 or dados==8:
            print('Você perdeu a Field, agora você tem {} fichas'.format(ficha))
            Field=False
        elif dados== 2:
            ficha=ficha+aposta2*3
            print('Você venceu a Field com um 2, agora você tem {} fichas'.format(ficha))
            Field=False
        elif dados== 12:
            ficha=ficha+aposta2*4
            print('Você venceu a Field com um 12, agora você tem {} fichas'.format(ficha))
            Field=False
        else:
            ficha=ficha+aposta2*2
            print('Você venceu a Field, agora você tem {} fichas'.format(ficha))
            Field=False
#Aposta de Any_Craps
    if Any_Craps:
        if dados==2 or dados==3 or dados==12:
            ficha = aposta3*8 + ficha
            print('Você venceu a Any_Craps, agora você tem {} fichas'.format(ficha))
            Any_Craps = False
        else:
            print('Você perdeu a Any_Craps, agora você tem {} fichas'.format(ficha))
            Any_Craps = False


#Aposta de Twelve
    if Twelve:
        if dados==12:
            ficha = aposta4*31 + ficha
            print('Você venceu a Twelve, agora você tem {} fichas'.format(ficha))
            Twelve = False
        else:
            print('Você perdeu a Twelve, agora você tem {} fichas'.format(ficha))
            Twelve = False
    print ("Valor do 1º dado -> ", dado1)
    print ("Valor do 2º dado -> ", dado2)
    print('Soma do valor dos dados jogados:{}'.format(dados))

#Faze de Point
    if Point:
        print(' Na fase Point. Você pode fazer as seguintes apostas: Field, Any Craps, Twelve.')
        resposta=input('Quer fazer mais alguma aposta?(s/n):')
        if resposta=='s':
            resposta=input('Você deseja fazer uma Field:(s/n):')
            if resposta=='s':
                Field=True
                aposta2=int(input('Quanto você vai apostar?'))
                ficha=ficha-aposta2    
            else:
                None
            resposta=input('Você deseja fazer uma Any Craps:(s/n):')
            if resposta=='s':
                    Any_Craps=True
                    aposta3=int(input('Quanto você vai apostar?'))
                    ficha=ficha-aposta3
            else:
                    None
            resposta=input('Você deseja fazer uma Twelve:(s/n):')
            if resposta=='s':
                Twelve=True
                aposta4=int(input('Quanto você vai apostar?'))
                ficha=ficha-aposta4
            else:
                None
        ponto=dados
        i=0
        acertou=False
        while not acertou:
            dado1=(randint(1,6))
            dado2=(randint(1,6)) 
            dados=dado1+dado2
            i+=1
            if dados == 7:
                print('Você perdeu o Point, agora você tem {0} fichas, O dado foi rolado {1} vezes'.format(ficha, i))
                Point=False
                acertou=True
            elif dados== ponto:
                    ficha=ficha+aposta1*2
                    print('Parabéns você venceu o Point, agora você tem {0} fichas /n O dado foi rolado {1}'.format(ficha, i))
                    Point=False
                    acertou=True
            else:
                None
    else:
        None                
#Repetições de apostas
    if Field:
            if dados==5 or dados==6 or dados==7 or dados==8:
                print('Você perdeu a Field, agora você tem {} fichas'.format(ficha))
                Field=False
            elif dados== 2:
                ficha=ficha+aposta2*3
                print('Você venceu a Field com um 2, agora você tem {} fichas'.format(ficha))
                Field=False
            elif dados== 12:
                ficha=ficha+aposta2*4
                print('Você venceu a Field com um 12, agora você tem {} fichas'.format(ficha))
                Field=False
            else:
                ficha=ficha+aposta2*2
                print('Você venceu a Field, agora você tem {} fichas'.format(ficha))
                Field=False
    if Any_Craps:
        if dados==2 or dados==3 or dados==12:
            ficha = aposta3*8 + ficha
            print('Você venceu a Any_Craps, agora você tem {} fichas'.format(ficha))
            Any_Craps = False
        else:
            print('Você perdeu a Any_Craps, agora você tem {} fichas'.format(ficha))
            Any_Craps = False
    if Twelve:
        if dados==12:
            ficha = aposta4*31 + ficha
            print('Você venceu a Twelve, agora você tem {} fichas'.format(ficha))
            Twelve = False
        else:
            print('Você perdeu a Twelve, agora você tem {} fichas'.format(ficha))
            Twelve = False
    print ("Valor do 1º dado -> ", dado1)
    print ("Valor do 2º dado -> ", dado2)
    print('Soma do valor dos dados jogados:{}'.format(dados))
#Esse e o último bloco do while de fichas
    resposta=input('Você vai querer continuar jogar?(s/n):')
    if resposta=='s':
        resposta=input('Você deseja fazer uma Pass Line Bet:(s/n):')
        if resposta=='s':
            Pass_Line_Bet=True
            aposta1=int(input('Quanto você vai apostar?'))
            ficha=ficha-aposta1
        resposta=input('Você deseja fazer uma Field:(s/n):')
        if resposta=='s':
            Field=True
            aposta2=int(input('Quanto você vai apostar?'))
            ficha=ficha-aposta2    
        else:
            None
        resposta=input('Você deseja fazer uma Any Craps:(s/n):')
        if resposta=='s':
                Any_Craps=True
                aposta3=int(input('Quanto você vai apostar?'))
                ficha=ficha-aposta3
        else:
                None
        resposta=input('Você deseja fazer uma Twelve:(s/n):')
        if resposta=='s':
            Twelve=True
            aposta4=int(input('Quanto você vai apostar?'))
            ficha=ficha-aposta4
        else:
            None
    else:
        print('Até a próxima!')
        break
    



