def calcProd(fromN,tonN ):
    prod = 1
    for i in range(fromN,tonN + 1):
        prod += (2 * i + 1)
    return prod
print(calcProd(1, 11))
