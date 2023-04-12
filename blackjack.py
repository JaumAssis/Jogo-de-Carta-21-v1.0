import random

baralho = [1,2,3,4,5,6,7,8,9,10,10,10]
tracosep = ('-=')*20

print(f"{tracosep}\n        BEM-VINDO(A) AO JOGO 21!\n{tracosep}")

p1 = int(input("\nDIGITE: \n[1] PARA JOGAR\n[2] PARA SAIR\nLembrando que durante o jogo, digite s caso queira mais cartas ou n caso deseje parar.\n>> "))

p2 = total = x = 0
if p1 == 1:
        print("\nINICIANDO...")
elif p1 == 2:
        print("\nSAINDO...\nAté a Proxíma!")
        quit()
while p2 != "N":
    
    x = random.choice(baralho)

    total += x

    if total > 21:
        print(f'\nVocê PERDEU!\nAs somas das cartas escolhidas foi {total} e PASSOU de 21!')
        break    

    
    if total == 21:
        print(f'\nPARABÉNS!\n As soma das cartas escolhidas foi exatamente o número {total}')
        break
    
    print("\nSua carta é", x)
    p2 = str(input(f"Você quer mais cartas?\nVocê possui {total} pontos no momento.\n>> ").upper())
    
    
    if p2 == 'N':
        print(f'\nQuase lá!\n As soma das cartas escolhidas foi {total} e deu menos que 21!')
        break
