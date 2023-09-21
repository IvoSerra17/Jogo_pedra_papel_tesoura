import random
pc_list = movie_list = ["Pedra","Papel","Tesoura"]
pc = random.choice(pc_list)
print(pc)

x=input("Escolha a sua jogada: ")

if pc == x:
    print("Empatou")
elif pc == "Pedra" and x == "Papel":
    print("Venceu")
elif pc == "Papel" and x == "Tesoura":
    print("Venceu")
elif pc == "Tesoura"and x == "Pedra":
    print("Venceu")
else:
    print("Perdeu")
