import math
import pylab
import numpy

def f(x):
	return math.exp(x) - math.acos(math.sqrt(x))

def df(x):
	return math.exp(x) * math.ln(math.exp(1)) + 1 / (pow(-x, 2) + 4)

def g(x):
	return x - 1 / .2 * f(x)
	
def method_of_chords(a, b, eps):
	print("Method of chords: ")
	n = 0
	while abs((b - a)) > eps:
		a = b - (f(b) / (f(b) - f(a))) * (b - a) 
		b = a + (f(a) / (f(a) - f(b))) * (a - b)
		n = n + 1
		print("iteration #", n, ": ", b)
	
def aitkens_method(x0, eps):
	print("Aitkens method:")
	n = 0
	while True:
		x1 = g(x0)
		x2 = g(x1)
		x2s = (x0 * x2 - pow(x1, 2)) / (x2 - 2 * x1 + x0)
		x3 = g(x2s)
		n = n + 1
		print("iteration #", n, ": ", x3)
		if abs(f(x3)) <= eps:
			break
		else:
			x0 = x2s
			x1 = x3
			x2 = g(x1)

def steffensens_methos(x0, eps):
	print("Steffensens method: ")
	n = 0
	while True:
		n = n + 1
		x1 = x0 - pow(f(x0), 2) / (f(x0) - f(x0 - f(x0)))
		print("iteration #", n, ": ", x1)
		if abs(f(x1)) > eps:
			x0 = x1
		else: 
			break
	
	
def drow():
	X = numpy.arange(0, 1, .01)
	pylab.plot([x for x in X], [f(x) for x in X])
	pylab.grid()
	pylab.show()

drow()	
a = 0.1
b = 0.2
eps = .00001
x0 = .16

method_of_chords(a, b, eps)
aitkens_method(x0, eps)
steffensens_methos(x0, eps)