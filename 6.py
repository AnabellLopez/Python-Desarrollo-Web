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
