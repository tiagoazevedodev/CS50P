import random


def main():
    acertos = 0
    level = get_level()
    for i in range(10):
        pergunta, resposta = generate_integer(level)
        cont = 0
        while True:
            cont += 1
            tentativa = input(pergunta)
            if tentativa == str(resposta):
                acertos += 1
                break
            elif cont == 3:
                print("EEE")
                print(f"{pergunta}{resposta}")
                break
            else:
                print("EEE")
                continue
    print(f"Score: {acertos}")


def get_level():
    while True:
        level = (input("Level: "))
        if level == "1" or level == "2" or level == "3":
            return level
        else:
            continue


def generate_integer(level):
    if level == "1":
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        resposta = x + y
    elif level == "2":
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        resposta = x + y
    elif level == "3":
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        resposta = x + y

    pergunta = f"{x} + {y} = "
    return pergunta, resposta


if __name__ == "__main__":
    main()
