"""
-Start with 2 letters OK
-Max of 6 Char's OK
-Numbers cannot be in between of letters, and 0 cannot be the first number used
-No spaces, and special characters are allowed OK
-All inputs will be uppercase ok
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.isalnum() and len(s) >= 2 and len(s) <= 6 and s[0:2].isalpha():
        for char in s:
            if char.isdigit():
                index = s.index(char)
                if s[index:].isdigit() and int(char) != 0:
                    return True
                else:
                    return False
        return True

main()
