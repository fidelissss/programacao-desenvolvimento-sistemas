from random import randint 

num = randint(1,10)
tentativas = None
user_input = None
dif = int(input("\nDigite a dificuldade que deseja jogar:\n[1]Fácil : 8 Tentativas\n[2]Médio : 5 Tentativas\n[3]Difícil : 3 Tentativas\n\n"))

if dif == 1:
    tentativas = 8
elif dif == 2:
    tentativas = 5
else:
    tentativas = 3

for i in range(tentativas):
    user_input = int(input("Pense em um número e digite : "))
    if  user_input == num:
        print("[!]Vocẽ acertou!")
        break
    else:
        if user_input < num:
            print("[x]Você errou, o número secreto é maior! Tente novamente!\n[!]Tentativas restantes:", tentativas -1 - i, "\n")
        else:
            print("[x]Você errou, o número secreto é menor! Tente novamente!\n[!]Tentativas restantes:", tentativas -1 - i, "\n")

            