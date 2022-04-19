def ascii(ch1,ch2):
    for i in range (ord(ch1)+1,ord(ch2)):
        print(chr(i), end = " ")


char1 =input()
char2 =input()

ascii(char1,char2)