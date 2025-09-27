# %%
import random

print("Olá, bem vindo!")

num_fosforos=21
ordem=input("Pretende jogar primeiro? Sim ou Não?")

if ordem== "Sim" or ordem=="S" or ordem== "sim" or ordem =="s":

    #while que controla o jogo todo
    while num_fosforos>=1:

        #jogada do jogador
        invalido=True
        while invalido:
            jogada=int(input("Entre 1 e 4, escolha o número de fósforos que deseja retirar."))
            if (jogada<=4 and jogada>=1):
                if jogada> num_fosforos:
                    print(f"A jogada é ilegal.")
                else:
                    num_fosforos= num_fosforos - jogada
                    invalido=False
                    print(f"O jogador tirou {jogada} fósforos.")
                    print(f"O número de fósforos que sobra é: {num_fosforos}")
            else:
                print(f"A jogada é ilegal.")


        
        #jogada do computador

        if num_fosforos>0:
            print("O computador vai jogar.")

            #se o jogador fizer a melhor jogada (se sobrar um múltiplo de 5)
            if num_fosforos%5== 0:
                num_aleatorio= random.randint(1,4 )
                num_fosforos= num_fosforos - num_aleatorio
                #num_fosforos-=num_aleatorio
                print(f"O PC tirou {num_aleatorio} fósforos.")
                print(f"O número de fósforos que sobra é: {num_fosforos}")

            else:
                num_computador= num_fosforos  - int( num_fosforos/5) * 5
                num_fosforos-= num_computador
                print(f"O PC tirou {num_computador} fósforos.")
                print(f"O número de fósforos que sobra é: {num_fosforos}")

                if num_fosforos==0:
                    print("O computador ganhou.")
        
        
        else:
            print("O jogador ganhou.")

else:
     print("Resposta não válida.")

if ordem=="Não" or ordem=="N" or ordem== "não" or ordem =="n":
     while num_fosforos>=1:
         
        #jogada do computador

        num_pc= num_fosforos  - int( num_fosforos/5) * 5
        if (num_pc<=4 and num_pc>=1):
            num_fosforos-= num_pc
            print(f"O PC tirou {num_pc} fósforos.")
            print(f"O número de fósforos que sobra é: {num_fosforos}")
        else:
            print("A jogada é ilegal.")


        #jogada do jogador
        if num_aleatorio<num_fosforos:
            num_aleatorio= random.randint(1,4 )
            num_fosforos= num_fosforos - num_aleatorio
            #num_fosforos-=num_aleatorio
            print(f"O jogador tirou {num_aleatorio} fósforos.")
            print(f"O número de fósforos que sobra é: {num_fosforos}")
        else:
            print("O computador ganhou.")

else:
    pass