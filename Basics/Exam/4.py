n_adresses = int(input())
m_adresses = int(input())
s_adresses = int(input())

magic_number=False
for numbers in range(m_adresses, n_adresses - 1,-1):
    if numbers % 2 ==0 and numbers % 3 ==0:
        magic_number = True
        if numbers == s_adresses:
            break
        print(numbers, end=' ')