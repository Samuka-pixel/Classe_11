from random import randint

Op = str(input("Pedra papel or tesoura?"))
list = ["Pedra", "Papel", "Tesoura"]
rand = randint(0, 2)
print(list[rand])
