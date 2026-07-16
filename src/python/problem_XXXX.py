sqeres = []
for base in range(984000):
    if (base**2) %2 != 0:
        sqeres.append(base**2)
print(sum(sqeres))