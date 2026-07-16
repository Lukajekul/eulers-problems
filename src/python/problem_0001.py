multiples = []
for devident in range(1000):
    if (devident % 3 == 0 or devident % 5 == 0) and devident not in multiples:
        multiples.append(devident)
print(sum(multiples))