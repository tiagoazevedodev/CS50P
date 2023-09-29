#99 ou mais F, 1 ou menor E
while True:
    try:
        numerador, divisor = (input("Fraction: ")).split("/")
        porcento = (int(numerador)/int(divisor))*100
        porcento = round(porcento)

        if int(porcento) > 100:
            continue
        elif int(porcento) >= 99:
            print("F")
            break
        elif int(porcento) <= 1:
            print("E")
            break
        else:
            print(f"{porcento}%")
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass