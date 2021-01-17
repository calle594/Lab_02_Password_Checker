def check_strength(passwd):
    """check strength of password"""
    if len(passwd) < 6:
        return False

    # check password for upperase, lowercase and numeric chars
    hasupper = False
    haslower = False
    digitcount = 0

    for c in passwd:
        if c.isupper():
            hasupper = True
        elif c.islower():
            haslower = True
        elif c.isdigit():
            digitcount = digitcount + 1

    if hasupper and haslower and digitcount >= 3:
        return True

def main():
    #ask for user input
    passwd = input("Enter your password: ")
    result = check_strength(passwd)
    #print the result
    if result: print(f'Password{passwd} is strong')
    else: print (f'Password {passwd} is not strong')

if __name__ == '__main__':
    main()