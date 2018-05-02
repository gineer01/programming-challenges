LIMIT = 21 * 2
uglies = []
MAX = 2**LIMIT
for i in range(LIMIT):
    for j in range(LIMIT):
        product = 2 ** i * 3 ** j
        if product > MAX:
            break

        while product < MAX:
            uglies.append(product)
            # print(i, j, product)
            product *= 5

uglies.sort()
print(uglies)
print(len(uglies))
print("The 1500'th ugly number is %d." % uglies[1500 - 1])