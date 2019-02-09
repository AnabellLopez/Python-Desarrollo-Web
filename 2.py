#Fibonacci
def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
def print_fibo(n):
    for i in range(n):
        print(fibonacci(i), end=' ')

n = int(input())
print_fibo(n)

#Ejercicio 1
r = int(input())
for i in range (1,r+1):
    s = (10 ** i) - 1
    print(s)

#Ejercicio 2
r = int(input())
for i in range (1, r+1):
    r = ((10 ** i) - 1) // 9
    print (r ** (2))