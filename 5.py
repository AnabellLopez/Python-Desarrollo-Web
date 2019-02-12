# Enter your code here. Read input from STDIN. Print output to STDOUT
S = input()
r = []
R = []
NP = []
NI = []
for i in S:
    if i.isdigit() == False and i >= "a" and i <= "z":
        k = ord(i)
        r.append(k)
    if i.isdigit() == False and i >= "A" and i <= "Z":
        K = ord(i)
        R.append(K)
    if i.isdigit() == True and int(i) % 2 == 0:
        NP.append(i)
    if i.isdigit() == True and int(i) % 2 != 0:
        NI.append(i)
l = sorted(r)
L = sorted(R)
NP = sorted(NP)
NI = sorted(NI)
r.clear()
R.clear()
for i in l:
    k = chr(i)
    r.append(k)
for i in L:
    K = chr(i)
    R.append(K)
str1 = ''.join(r) + ''.join(R) + ''.join(NI) + ''.join(NP)
print(str1)