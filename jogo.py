import random
print("SEJA MUITO BEM VINDO AO JOGO DE ADIVINHAÇÃO")
numerosecreto = random.randint(1,10)
tentativas = 0
max_tentativas = 3 


while tentativas < max_tentativas :
    palpite = int(input("Tente adivinhar o número entre 1 e 10: "))
    tentativas += 1 
    if tentativas == max_tentativas:
        print("Você perdeu!!O número era." , numerosecreto)
        break
    if palpite < numerosecreto:
        print( "Muito baixo.Tente novamente!!")

    elif palpite > numerosecreto:
        print("Muito alto.Tente novamente!!")

    else:
        print("Você acertou o número!")