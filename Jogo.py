#Inicio do Jogo
print('Bem vindo(a) ao Kassinão!')
print('Já que é a sua primeira vez toma aí 1000 fichas')
print('Bora jogar Craps')

#Variaveis
ficha=1000
Pass_Line=False
Field=False
Any_Craps=False
Twelve=False
#Roladoe de dados
dados=0

#Resposta do user
resposta=input('Você vai querer jogar?(s/n)')
if resposta=='s':
    print('Agora estamos no Come Out. Você pode fazer as seguintes apostas: Pass Line Bet, Field, Any Craps, Twelve.')
    tipo=input('Qual vai ser o tipo da aposta:')
    aposta=int(input('Quantas fichas você vai apostar:'))
    ficha-=aposta
    resposta=input('Quer fazer mais alguma aposta?(s/n)')
    while resposta=='s':
        tipo=input('Qual vai ser o tipo da aposta:')
        aposta=int(input('Quantas fichas você vai apostar:'))
        ficha-=aposta
        tipo=True
        resposta=input('Quer fazer mais alguma aposta?(s/n)')
else:
    print('Até a proxima!')

#Aposta pass line bet
if Pass_Line:
    Point=False
    if dados == 7 or 11:
        ficha+=aposta*2
        print('Parabéns você ganhou, agora você tem {} fichas.'.format(ficha))
        Pass_Line=False
    elif dados == 2 or 3 or 12:
        print('Infelizmente você perdeu, agora você tem {} fichas'.format(ficha))
        Pass_Line=False
    else:
        print('Saiu {0} nos dados agora estamos na faze de Point')
        Pass_Line=False
        Point=True
        #Faze de Point
        if Point:
            print('Agora estamos no Point. Você pode fazer as seguintes apostas: Field, Any Craps, Twelve.')
            resposta=input('Quer fazer mais alguma aposta?(s/n)')
            while resposta=='s':
                tipo=input('Qual vai ser o tipo da aposta:')
                aposta=int(input('Quantas fichas você vai apostar:'))
                ficha-=aposta
                tipo=True
                resposta=input('Quer fazer mais alguma aposta?(s/n)')
            ponto=dados
            dados=10
            i=0
            while dados!=ponto or 7:
                dados=0
                i+=1
            if dados== 7
            print('Você perdeu, agora você tem {0} fichas /n O dado voi rolado {1}'.format(ficha, i))



