import inflect

names = []
p = inflect.engine()

while True:
    try:
        entrada = input("Name: ")
        names.append(entrada)
    except EOFError:
        print()
        break

count = len(names)

if count == 1:
    farewell = f"Adieu, adieu, to {names[0]}"
elif count == 2:
    farewell = f"Adieu, adieu, to {names[0]} and {names[1]}"
else:
    names_except_last = ", ".join(names[:-1])
    last_name = names[-1]
    farewell = f"Adieu, adieu, to {names_except_last}, and {last_name}"

print(farewell)
