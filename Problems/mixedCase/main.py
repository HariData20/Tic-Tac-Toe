s = input().split()

for i in range(0, len(s)):
    if i == 0:
        s[i] = s[i].lower()
    else:
        s[i] = s[i].capitalize()
print(''.join(s))






