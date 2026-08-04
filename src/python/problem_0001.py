###
# MULTIPLES OF 3 AND 5
###

# check if the devident is a multiple of 3 or 5 and adds it into a list that gets summed up at the end print

multiples = []
for devident in range(1000):
    if (devident % 3 == 0 or devident % 5 == 0):
        multiples.append(devident)
print(sum(multiples))