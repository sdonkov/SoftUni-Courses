def parse(word):
    temp = ''
    for ch in word:
        if ch.isdigit():
            temp+=ch

    ascii = int(temp)
    char_value = chr(ascii)
    new_word = word.replace(temp,char_value)
    return new_word

def replace(word):
    str=''
    temp = list(word)
    temp[1],temp[-1] = temp[-1], temp[1]
    return "".join(temp)


def sum(word):
    res = parse(word)
    res = replace(res)
    return res

words = input().split()
new_word = [sum(word) for word in words]
print(" ".join(new_word))
