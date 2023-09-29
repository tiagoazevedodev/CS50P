#input do valor
#testar se é 25,10,5. Se não for mandar input denovo
#testar de já passou de 50, se passou printar quanto deve de troco
#printar a quantidade que falta pra comprar a coca
#input pra ele botar mais moedas
valor = 0
falta = 50
while valor < 50:
    print(f"Amount Due: {falta}")
    insert = int(input("Insert Coin: "))
    if insert == 25 or insert == 10 or insert == 5:
        valor = valor + insert
        falta = falta - insert
        if falta <= 0:
            falta = falta * -1
            print(f"Change Owed: {falta}")
        else:
            continue
    else:
        continue






