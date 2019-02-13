#You are given a space separated list of nine integers. Your task is to convert this list into a 3x3 NumPy array.
import numpy
S = input()
L = list(map(int, S.split(" ")))
my_array = numpy.array(L)
print(numpy.reshape(my_array,(3,3)))
