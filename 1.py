#bisiesto
n = input()
if (int(n) % 4 == 0 and int(n) % 100 != 0) or int(n) % 400 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")


#Lista de n�meros
up= 1
while up < 101:
    print (up, end = ' ')
    up += 1

#Calculadora de n�meros primos
X = input()
X = int(X)
if (X == 2 or X == 3 or X == 5 or X == 7) or (X % 2 != 0 and X % 3 != 0 and X % 5 != 0 and X % 7 != 0) and (X != 1):
    print ("el n�mero " + str(X) + " es primo")
else:
    print("el n�mero " + str(X) + " NO es primo")

#binarios
v = input()
v = int(v)
s = ""
while (v // 2) > 1:
    r = v % 2
    s += str(r)
    v = v // 2
if v // 2 == 1:
    s = s + str(v % 2) + str("1")
Q = str(s[::-1])
print(Q)