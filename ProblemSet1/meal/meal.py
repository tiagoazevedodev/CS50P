#eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?
'''
h, min = input("What time is it? ").split(":")
h = int(h)
min = int(min)
if h == 7 and min >= 00 and min < 60 or h == 8 and min == 00:
    print("breakfast time")
if h == 12 and min >= 00 and min < 60 or h == 13 and min == 00:
    print("lunch time")
if h == 18 and min >= 00 and min < 60 or h == 19 and min == 00:
    print("dinner time")
'''
def main():
    time = input("What time is it? ")
    converted = convert(time)
    if converted >= 7 and converted <= 8:
        print("breakfast time")
    elif converted >= 12 and converted <= 13:
        print("lunch time")
    elif converted >= 18 and converted <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours) + (float(minutes) / 60)
    return hours

if __name__ == "__main__":
    main()