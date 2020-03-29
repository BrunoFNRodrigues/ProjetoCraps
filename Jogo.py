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
aposta1=0
aposta2=0
aposta3=0
aposta4=0
#Roladoe de dados
dados=6

#Resposta do user
resposta=input('Você vai querer jogar?(s/n)')
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
    else:
        None
    resposta=input('Você deseja fazer uma Any Craps:(s/n):')
    if resposta=='s':
        Any_Craps=True
        aposta3=int(input('Quanto você vai apostar?'))
    else:
        None
    resposta=input('Você deseja fazer uma Twelve:(s/n):')
    if resposta=='s':
        Twelve=True
        aposta4=int(input('Quanto você vai apostar?'))
    else:
        None
else:
    print('Até a próxima!')

while not ficha==0:
    resposta=input('Você vai querer continuar jogar?(s/n)')
    if resposta=='s':
        print('Agora estamos no Come Out. Você pode fazer as seguintes apostas: Pass_Line_Bet, Field, Any_Craps, Twelve.')
        resposta=input('Você deseja fazer uma Pass Line Bet:(s/n):')
        if resposta=='s':
            Pass_Line_Bet=True
        else:
            None
        resposta=input('Você deseja fazer uma Field:(s/n):')
        if resposta=='s':
            Field=True
        else:
            None
        resposta=input('Você deseja fazer uma Any Craps:(s/n):')
        if resposta=='s':
            Any_Craps=True
        else:
            None
        resposta=input('Você deseja fazer uma Twelve:(s/n):')
        if resposta=='s':
            Twelve=True
        else:
            None
    #Aposta pass line bet
    if Pass_Line_Bet:
        Point=False
        if dados == 7 or 11:
            ficha=ficha+aposta*2
            print('Parabéns você ganhou, agora você tem {} fichas.'.format(ficha))
            Pass_Line_Bet=False
        elif dados == 2 or 3 or 12:
            print('Infelizmente você perdeu, agora você tem {} fichas'.format(ficha))
            Pass_Line_Bet=False
        else:
            print('Saiu {0} nos dados agora estamos na faze de Point'.format(dados))
            Pass_Line_Bet=False
            Point=True
            #Faze de Point
            if Point:
                print('Agora estamos no Point. Você pode fazer as seguintes apostas: Field, Any Craps, Twelve.')
                resposta=input('Quer fazer mais alguma aposta?(s/n)')
                while resposta=='s':
                    tipo=input('Qual vai ser o tipo da aposta:')
                    aposta=int(input('Quantas fichas você vai apostar:'))
                    ficha=aposta-ficha
                    tipo=True
                    resposta=input('Quer fazer mais alguma aposta?(s/n)')
                ponto=dados
                dados=10
                i=0
                while dados!= ponto or 7:
                    dados=10
                    i+=1
                if dados == 7:
                    print('Você perdeu, agora você tem {0} fichas /n O dado foi rolado {1}'.format(ficha, i))
                    Point=False
                else:
                    ficha=ficha+aposta*2
                    print('Parabéns você venceu, agora você tem {0} fichas /n O dado foi rolado {1}'.format(ficha, i))
                    Point=False

    if Field:
        if dados== 5 or 6 or 7 or 8:
            print('Você perdeu, agora você tem {} fichas'.format(ficha))
            Field=False
        elif dados== 2:
            ficha=ficha+aposta*3
            print('Você venceu com um 2, agora você tem {} fichas'.format(ficha))
            Field=False
        elif dados== 12:
            ficha=ficha+aposta*4
            print('Você venceu com um 12, agora você tem {} fichas'.format(ficha))
            Field=False
        else:
            ficha=ficha+aposta*2
            print('Você venceu, agora você tem {} fichas'.format(ficha))
            Field=False

            


