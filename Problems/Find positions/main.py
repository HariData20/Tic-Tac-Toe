# put your python code here
n = input().split()
find = input()
index = []
for i, _ in enumerate(n):
    if n[i] == find:
        index.append(f'{i}')

if len(index) ==0:
    print('not found')
else:
    print(' '.join(index))

prime_numbers = [n for n in range(2, 1000) if all(n % i != 0 for i in range(2, n - 1))]
