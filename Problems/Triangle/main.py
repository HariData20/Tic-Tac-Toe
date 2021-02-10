height = int(input())
no_of_symbols = height * 2 - 1
str1 = []
for i in range(1, height+1):
    str1.append('#' * ((i * 2)-1))
    print((str1[i-1].center(no_of_symbols)))



