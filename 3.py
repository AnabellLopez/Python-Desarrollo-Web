#Suma de datos

n = input()
sum_ = 0
for num in n:
for sum_ += int(num)
print (sum_)

#ordenar valores

li = list(map(int, input().split()))
n = len(li)
for j in range(n):
    ban = True
    for i in range(1, n - j):
        if li[i] < li[i - 1]:
            li[i], li[i - 1] = li[i - 1], li[i]
            ban = False
    if ban == True:
        break
print(li)

#segundo mayor valor

l = list(map(int, input().split()))
l.sort()
print(l[len(l)-2])

#metodo 2

l = list(map(int, input().split()))
may = may2 = min(l)
for e in l:
    if e > may:
        may2 = may
        may = e
    elif e > may2:
        may2 = e
r = [may, may2]
print(r)

#mayus a minus

inp = input()
r = inp.swapcase()
print(r)

#metodo2

inp = input()
r = ""
for i in inp:
    if i.islower():
        r += i.upper()
    else:
        r += i.lower()
print(r)

#contar palabras

c = input().split()
d = {}
for word in c:
    if d.get(word) == None:
        d[word]= 1
    else:
        d[word] += 1
for k, v in d.items():
    print(k, v)

#hallar número no repetido

nums = [2, 2, 4, 4, 5, 5, 6, 6, 7]
print(2 * sum(set(nums)) - sum(nums))
#otro
nums = [2, 2, 4, 4, 5, 5, 6, 6, 7]
d = {}
for i in nums:
    if d.get(i):
        del d[i]
    else:
        d[i] = 1
print(d.popitem()[0])


#Factorial y factorial_return

n = int(input())
def factorial (n):
    if n == 1 or n == 0:
        return 1
    else:
        fac = 0
        while n > 1:
            if fac == 0:
                fac = n * (n - 1)
            else:
                fac *= (n - 1)
            n -= 1
        return fac

factorial(n)

def factorial_return():
    if n == 1 or n == 0:
        return 1
    return (factorial(n-1)*n)

factorial_return()

#Ejercicio 1 calcular

n = int(input())
f = 0

def function(n, f):
    while n >= 1:
        if n % 2 == 0:
            f += n
        else:
            f -= n
        n -= 1
    return f

function(n, f)