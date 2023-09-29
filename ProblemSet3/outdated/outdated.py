months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    entrada = input("Data: ").strip()
    if "/" in entrada:
        entrada = entrada.strip()
        mes, dia, ano = entrada.split("/")
        if mes in months:
            continue
    elif "," in entrada:
        entrada = entrada.split(",")
        ano = entrada[1].strip()
        mes, dia = entrada[0].split(" ")
        if mes in months:
            mes = months.index(mes) + 1
        else:
            continue
    else:
        continue
    if int(dia) > 31 or int(mes) > 12:
        continue
    else:
        break
print(f"{ano}-{str(mes).zfill(2)}-{str(dia).zfill(2)}")