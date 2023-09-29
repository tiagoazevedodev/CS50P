itens = {}
while True:
    try:
        new_item = input().upper()
        if new_item in itens.keys():
            itens[new_item] += 1
        else:
            itens[new_item] = 1
    except EOFError:
        sorted_items = sorted(itens.items(), key=lambda x: x[0])
        for chave, valor in sorted_items:
            print(valor, chave)
        break
