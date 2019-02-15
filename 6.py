#You are given a space separated list of nine integers. Your task is to convert this list into a 3x3 NumPy array.
import numpy
S = input()
L = list(map(int, S.split(" ")))
my_array = numpy.array(L)
print(numpy.reshape(my_array,(3,3)))
#You are given a NxM integer array matrix with space separated elements (N = rows and M = columns).Your task is to print the transpose and flatten results.
import numpy
N, M = input().split(" ")
L = []
for i in range(int(N)):
    S = list(map(int, input().split(" ")))
    L.append(list(S))
my_array = numpy.array(L)
print(numpy.transpose(my_array))
print(my_array.flatten())
#You are given two integer arrays of size NxM and MxP ( N&M  are rows, and P is the column). Your task is to concatenate the arrays along axis 0.
import numpy
N, M, P = input().split(" ")
L = []
for i in range(int(N)+int(M)):
    S = list(map(int, input().split(" ")))
    L.append(list(S))
my_array = numpy.array(L)
print(numpy.reshape(my_array,(int(N)+int(M), int(P))))

# Zeros and Ones
import numpy
# c is optional here.
a,b,*c = map(int,input().split())
print(numpy.zeros((a,b,*c),dtype=numpy.int))
print(numpy.ones((a,b,*c),dtype=numpy.int))

#Your task is to print an array of size NxM with its main diagonal elements as 1's and 0's everywhere else.
import numpy
N, M = input().split(" ")
print (str(numpy.eye(int(N), int(M), k = 0)).replace("1"," 1").replace("0"," 0"))

#You are given two integer arrays, A and B of dimensions NxM. Your task is to perform the following operations:
import numpy
N, M = input().split(" ")
A = []
B = []
for i in range(int(N)):
    S = list(map(int, input().split(" ")))
    A.append(S)
for i in range(int(N)):
    S = list(map(int, input().split(" ")))
    B.append(S)

A = numpy.array(A, int)
B = numpy.array(B, int)

print(str(numpy.add(A, B)).replace(".",""))
print(str(numpy.subtract(A, B)).replace(".",""))
print(str(numpy.multiply(A, B)).replace(".",""))
print(str(A // B).replace(".",""))
print(str(numpy.mod(A, B)).replace(".",""))
print(str(A ** B).replace(".",""))

#You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A.
import numpy

numpy.set_printoptions(sign=' ')

A = list(map(float, input().split(" ")))

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

#You are given a 2-D array with dimensions NxM. Your task is to perform the sum tool over axis 0 and then find the product of that result.
import numpy

N, M = input().split(" ")
A = []
for i in range(int(N)):
    S = list(map(int, input().split(" ")))
    A.append(S)
B = numpy.sum(A, axis = 0)
print(numpy.prod(B))
