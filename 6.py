import numpy
S = input()
L = list(map(int, S.split(" ")))
my_array = numpy.array(L)
print(numpy.reshape(my_array,(3,3)))