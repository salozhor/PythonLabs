import numpy as np
import matplotlib.pyplot as plt
from pylab import setp
def func1(x):
	return 5+0.5*x
	
def func2(x):
	return 16
	
def func3(x):
	return 2*x-1
	
def func4(x):
	return 0
	
def func5(x):
	return 2*x-1

def plotit(start, end, n):
	x = np.arange(start, end, n)
	y1 = np.array([func1(item) for item in x])
	y2 = np.array([func2(item) for item in x])
	y3 = np.array([func3(item) for item in x])
	y4 = np.array([func4(item) for item in x])
	y5 = np.array([func5(item) for item in x])
	plt.plot(x, y1, label = "x1 - 2x2 <= -10")
	plt.plot(x, y2, label = "x2 <= 16")
	plt.plot(x, y3, label = "2x1 - x2 <= 1")
	plt.plot(x, y4, label = "x2 >= 0")
	plt.plot(x, y5, label = "4x1 - 2x2 = 2")
	#line0 = plt.plot(x2, y2)
	#setp(line0, linewidth=1, color='y')
	

	plt.grid()
	plt.legend()
	plt.show()

start, end, n = -100, 100, 1
plotit(start, end, n)