from random import randint
level = -1

while level <= 0:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
sorteado = randint(0,level)

while True:
    try:
        tentativa = (input("Guess: "))
        if int(tentativa) == sorteado:
            print("Just right!")
            break
        elif int(tentativa) > sorteado:
            print("Too large!")
            continue
        elif int(tentativa) < sorteado:
            print("Too small!")
            continue
    except ValueError:
        continue
