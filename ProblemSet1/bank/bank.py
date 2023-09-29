#If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
greet = input("Greeting: ").strip().lower()
if "hello" in greet:
    print("$0")
elif greet.startswith("h") == True:
    print("$20")
else:
    print("$100")

