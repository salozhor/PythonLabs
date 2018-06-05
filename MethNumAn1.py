import numpy as np
import matplotlib.pyplot as plt
from math import log
from math import fabs
from pylab import setp

def func(x):
	qwe=(2*x-x**2)
	return log(qwe)+2-(x**0.5)
	
def plotfunc(f,xrange):
	yrange = [f(x) for x in xrange]
	graph = plt.plot(xrange,yrange)
	setp(graph, linewidth=0.5, color='b')
	
	plt.grid()
	plt.show()
	
def minmod(a,b):
	a=fabs(a)
	b=fabs(b)
	if (a>=b): return True
	return False
	
def checkEps(a):
	if (fabs(a)<=0.00001): 
		print("fabs = ", fabs(a))
		return True
	return False
	
def bisectionMethod(a,b):
	
	fa = func(a)
	fb = func(b)
	if (checkEps(fa)): 
		return a
	if (checkEps(fb)):
		return b
	c = (a + b) / 2
	fc = func(c)
	if ((fc>0 and fa<0) or (fc<0 and fa>0)): return bisectionMethod(a,c)
	if ((fc>0 and fb<0) or (fc<0 and fb>0)): return bisectionMethod(c,b)
	if (fc==0): return c
	return "Error"
	

xs = np.arange(0.00001, 2, 0.00001)
plotfunc(func, xs)
print(bisectionMethod(0.00001,1))
print(bisectionMethod(1,1.99999))


