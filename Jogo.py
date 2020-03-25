#Inicio do Jogo
print('Bem vindo(a) ao Kassinão!')
print('Já que é a sua primeira vez toma aí 1000 fichas')
print('Bora jogar Craps')
resposta=input('Você vai querer jogar?s/n')
if resposta=='s':
    print('Agora estamos no Come Out. Você pode fazer as seguintes apostas: Pass Line Bet, Field, Any Craps')
    tipo=input('Qual vai ser o seu tipo de aposta:')
    aposta=int(input('Quantas fichas você vai apostar:'))
    ficha=1000
else:
    print('Até a proxima!')

Pass_Line=False
Field=False
Any_Craps=False
Twelve=False
if tipo==""
