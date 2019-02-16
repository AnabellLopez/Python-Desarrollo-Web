#bisiesto
n = input()
if (int(n) % 4 == 0 and int(n) % 100 != 0) or int(n) % 400 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")


#Lista de números
up= 1
while up < 101:
    print (up, end = ' ')
    up += 1

#Calculadora de números primos
X = input()
X = int(X)
if (X == 2 or X == 3 or X == 5 or X == 7) or (X % 2 != 0 and X % 3 != 0 and X % 5 != 0 and X % 7 != 0) and (X != 1):
    print ("el número " + str(X) + " es primo")
else:
    print("el número " + str(X) + " NO es primo")

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

#Read a given string, change the character at a given index and then print the modified string.
def mutate_string(string, position, character):
    return s[:int(i)] + c + s[int(i)+1:]
if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new

#In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.    
def count_substring(string, sub_string):
return len([i for i in range(len(string)) if string[i:i+len(sub_string)] == sub_string])

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
