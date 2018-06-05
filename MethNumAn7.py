from pylab import plot, show, grid
from numpy import arange, linalg, array
import sys

def l(xi, i, X, x0):
	n = len(X) - 1
	prod = 1
	for j in range(0, n):
		if i == j:	
			continue
		else:
			prod = prod * (x0 - X[j]) / (xi - X[j])
	return prod

def lagrange(X, Y, x0):
	n = len(X) - 1
	sum = 0
	for i in range(0, n):
		sum = sum + Y[i] * l(X[i], i, X, x0)
	return sum
	
def aitken(X, Y, i, j, x0):
	if j - i != 1:
		matrix = array([[x0 - X[i], aitken(X, Y, i, j - 1, x0)], [x0 - X[j], aitken(X, Y, i + 1, j, x0)]])
	else:
		matrix = array([[x0 - X[i], Y[i]], [x0 - X[j], Y[j]]])
	result = 1 / (X[j] - X[i]) * linalg.det(matrix)
	return result
	
X = [.41, .46, .52, .60, .65, .72]
Y = [2.57418, 2.32513, 2.09336, 1.86203, 1.74926, 1.62098]
x0 = 0.665

y0 = (x0 - X[4]) * (Y[5] - Y[4]) / (X[5] - X[4]) + Y[4]

X1 = arange(.41, .72, .001)
Y1 = lagrange(X, Y, X1)

n = len(X) - 1
n1 = len(X1) - 1
plot(X, Y, X, Y, '.r', X1, Y1, x0, aitken(X, Y, 0, n, x0), '.g', x0, y0, '.y')

grid()
show()
print(aitken(X, Y, 0, n, x0))
print(y0)
