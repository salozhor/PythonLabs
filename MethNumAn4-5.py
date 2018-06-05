from numpy import arange, array, linalg
from sympy import diff, symbols, sin, cos, tan

def f1(x0, y0):
	return sin(x0) + 2*y0 - 2

def f2(x0, y0):
	return cos(y0 - 1) + x0
	
def d(func, x0, y0, v):
	x, y = symbols('x y')
	return float(diff(func(x, y), v).subs([(x, x0),(y, y0)]))
	
def plotit(xrange):
	yrange1 = [f1(x) for x in xrange]
	yrange2 = [f2(x) for x in xrange]
	graph1 = plt.plot(xrange,yrange1)
	setp(graph1, linewidth=0.5, color='b')
	graph2 = plt.plot(xrange,yrange2)
	setp(graph2, linewidth=0.5, color='b')
	
	plt.grid()
	plt.show()
	
def iteration_method(x0, y0, eps):
	matrix = array([[d(f1, x0, y0, 'x'), d(f2, x0, y0, 'x')], [d(f1, x0, y0, 'y'), d(f2, x0, y0, 'y')]])
	lyambda_11_12 = linalg.solve(matrix, array([-1., 0.]))
	lyambda_21_22 = linalg.solve(matrix, array([0., -1.]))
	
	(l11, l12, l21, l22) = (lyambda_11_12[0], lyambda_11_12[1], lyambda_21_22[0], lyambda_21_22[1])
	while True:
		x1 = x0 + l11 * f1(x0, y0) + l12 * f2(x0, y0)
		y1 = y0 + l21 * f1(x0, y0) + l22 * f2(x0, y0)
		if abs(f1(x1, y1)) <= eps and abs(f2(x1, y1)) <= eps:
			print(x1, y1)
			break
		else:
			(x0, y0) = (x1, y1)

def newtons_method(x0, y0, eps):
	while True:
		matrix_w = array([[d(f1, x0, y0, 'x'), d(f1, x0, y0, 'y')], [d(f2, x0, y0, 'x'), d(f2, x0, y0, 'y')]], dtype = float)
		matrix_w1 = array([[-f1(x0, y0), d(f1, x0, y0, 'y')], [-f2(x0, y0), d(f2, x0, y0, 'y')]], dtype = float)
		matrix_w2 = array([[d(f1, x0, y0, 'x'), -f1(x0, y0)], [d(f2, x0, y0, 'x'), -f2(x0, y0)]], dtype = float)
		
		delta1 = linalg.det(matrix_w1) / linalg.det(matrix_w)
		delta2 = linalg.det(matrix_w2) / linalg.det(matrix_w)
		
		x0 = x0 + delta1
		y0 = y0 + delta2
		if abs(f1(x0, y0)) <= eps and abs(f2(x0, y0)) <= eps:
			print(x0, y0)
			break
		
eps = .001
x0 = .5
y0 = -.1
iteration_method(x0, y0, eps)
newtons_method(x0, y0, eps)
