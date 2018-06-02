import numpy
from tabulate import tabulate

# inicialna distribucija
v = numpy.array([[1.0, 0.0]])
# transakcijska metrika
T = numpy.array([[0.90, 0.10],
              [0.50, 0.50]])

# po n korakih
T_3 = numpy.linalg.matrix_power(T, 3)
T_50 = numpy.linalg.matrix_power(T, 50)
T_100 = numpy.linalg.matrix_power(T, 100)

#Printing the matrices
print("T_3: ")
print(tabulate(numpy.dot(v, T_3)))
print("T_50: ")
print(tabulate(numpy.dot(v, T_50)))
print("T_100: ")
print(tabulate(numpy.dot(v, T_100)))
