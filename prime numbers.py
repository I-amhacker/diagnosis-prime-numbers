n = 100
Prime = True
for x in range(2, n):
    if n % x == 0:
        Prime = False
if Prime:
    print("it is prime")
else:
    print("not prime")