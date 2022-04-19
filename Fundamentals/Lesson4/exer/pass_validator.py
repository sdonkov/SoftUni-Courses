SpecialSym =['$', '@', '#', '%']


def password(passwd):
    val = True
    if len(passwd) <6 or len(passwd)>10:
        print("Password must be between 6 and 10 characters")
        val = False
    # if not any(char.isdigit() for char in passwd):
    #     print('Password should have at least one numeral')
    #     val = False
    if any(char in SpecialSym for char in passwd):
        print("Password must consist only of letters and digits")
        val = False
    if sum(map(str.isdigit, passwd)) < 2:
        print ("Password must have at least 2 digits")
        val = False
    if val == True:
        print("Password is valid")

passwd = input()
password(passwd)