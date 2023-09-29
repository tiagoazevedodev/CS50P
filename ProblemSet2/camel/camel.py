#input: tiagoRodrigues output: tiago_rodrigues
camelcase = input("name as camelCase: ")

snake_case = ""
for digit in range(len(camelcase)):
    if camelcase[digit].isupper():
        snake_case = snake_case + "_" + camelcase[digit].lower()
    else:
        snake_case = snake_case + camelcase[digit]
print(snake_case)



