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

#Resposta do user
resposta=input('Você vai querer jogar?(s/n)')
if resposta=='s':
    print('Agora estamos no Come Out. Você pode fazer as seguintes apostas: Pass Line Bet, Field, Any Craps, Twelve.')
    tipo=input('Qual vai ser o tipo da aposta:')
    aposta=int(input('Quantas fichas você vai apostar:'))
    resposta=input('Quer fazer mais alguma aposta?(s/n)')
    while resposta=='s':
        tipo=input('Qual vai ser o tipo da aposta:')
        aposta=int(input('Quantas fichas você vai apostar:'))
        tipo=True
        resposta=input('Quer fazer mais alguma aposta?(s/n)')
else:
    print('Até a proxima!')

if tipo==""
