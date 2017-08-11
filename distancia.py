import math
def distancia(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("Distancia entre dos puntos\n")
x1 = float(input("Valor para x1: "))
y1 = float(input("Valor para y1: "))
x2 = float(input("Valor para x2: "))
y2 = float(input("Valor para y2: "))

r = distancia(x1, y1, x2, y2)
print("{0:.4f}".format(r))
