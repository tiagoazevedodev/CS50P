def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_stripped = d.strip('$')
    return float(d_stripped)


def percent_to_float(p):
    p_ready = p.strip('%')
    p_ready = float(p_ready)/100
    return p_ready


main()