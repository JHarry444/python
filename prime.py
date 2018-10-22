primes = []
for i in range(2, int(input("Enter max number: "))):
    factors = []
    for j in range(1, i + 1):
        if i % j == 0:
            factors.append(j)
    if len(factors) < 3:
        primes.append(i)
print(primes)
