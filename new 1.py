import numpy as np
import matplotlib.pyplot as plt


"""
ca - coefficients array
func - primordial function
plotit - creating primordial function plot
sty - starting values

"""



dy = [[0.0 for rweq in range(12)] for wqer in range(12)]

sty = [4.25562, 4.35325, 4.45422, 4.56184, 4.67344, 4.79038, 4.91306, 5.04192, 5.17744, 5.32016]
stx = np.arange(1.340, 1.390, 0.005)
irange = [9,8,7,6,5,4,3,2,1]
def fill_dy():
	noi = 0
	for i in irange:
		nod = 9-i
		for j in range(i):
			
				if nod == 0 :
					dy[nod][j]=round((sty[j]-sty[j+1])/(stx[j]-stx[j+1]),5)
				else:
					dy[nod][j]=round((dy[nod-1][j]-dy[nod-1][j+1])/(stx[j]-stx[j+10-i]),5)
	
			
			
def func(x):
	return sty(0)
	
	
def dy_show():
	for i in irange:
		nod = 9-i
		for j in range(i):
			print(dy[nod][j])
		print(" ")


def plotit(start, end, n, sty):
	x = np.arange(start, end, n)
	
	plt.plot(x, sty)
	plt.grid()

	plt.show()
	
def part(x, i):
	p=dy[i][0]
	for j in range(i+1):
		p *= x-stx[j]
	return p
	
		
	
def final_f(x):
	fnl = sty[0]
	for i in range(9):
		fnl = fnl + part(x, i)
	return fnl


start, end, n = 1.340, 1.390, 0.005
#plotit(start, end, n, sty)



fill_dy()
print(round(final_f(1.3473),5))
print(round(final_f(1.3763),5))
print(round(final_f(1.3583),5))
print(round(final_f(1.3812),5))
print(round(final_f(1.3787),5))
print(round(final_f(1.3455),5))




