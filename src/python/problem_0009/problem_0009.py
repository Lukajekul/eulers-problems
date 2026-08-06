###
# SPECIAL PYTHAGOREAN TRIPLET
### 

# Two for loops that look for a and b values that with the calculated value
# of c all sum up to 1000 for which stands that a < b < c. The ranges are 
# moddefied for efficency a cannot go to more then 333 for the reaon that that
# is already a third of 1000 and a needs to be smaller then b and c. Bs range
# starts with a + 1 for it needs to be larger and ends at 500 because it needs
# to be less then 499 (c). When the requerements are met their product gets
# printed out.

for a in range(1,334):
    for b in range(a+1,500):
        if a**2 + b**2 == (1000 - a - b)**2:
            print(a*b*(1000 - a - b))