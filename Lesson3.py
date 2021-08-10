def getPriceA():
    return a

def getPriceB():
    return b

def setPriceA(priceA):
    global a
    a = int(priceA)
    return

def setPriceB(priceB):
    global b
    b = int(priceB)
    return

def sum(pa, pb):
    return pa+pb

x = input("PriceA =")
setPriceA(x)
print(getPriceA())

y = input("PriceB =")
setPriceB(y)
print(getPriceB())

print(sum(getPriceA(), getPriceB()))