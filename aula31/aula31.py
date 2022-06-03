progressivo = 0
regressivo = 10

while progressivo <= 8:
    print(progressivo, regressivo)
    progressivo += 1
    regressivo -= 1

print('#####################')

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
