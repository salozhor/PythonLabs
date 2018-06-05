import numpy as np
import matplotlib.pyplot as plt
from pylab import setp

dy = [[0.0 for rweq in range(12)] for wqer in range(12)]

sty = [4.25562, 4.35325, 4.45422, 4.56184, 4.67344, 4.79038, 4.91306, 5.04192, 5.17744, 5.32016]
stx = np.arange(1.340, 1.390, 0.005)


tx = [1.3473, 1.3763, 1.3583, 1.3812, 1.3787, 1.3455]

irange = [9,8,7,6,5,4,3,2,1]
def fill_dy():
	
	for i in irange:
		nod = 9-i
		for j in range(i):
			
				if nod == 0 :
					dy[nod][j]=round((sty[j]-sty[j+1])/(stx[j]-stx[j+1]),5)
				else:
					dy[nod][j]=round((dy[nod-1][j]-dy[nod-1][j+1])/(stx[j]-stx[j+10-i]),5)
fill_dy()

#def dy_show():
#	for i in irange:
#		nod = 9-i
#		for j in range(i):
#			print(dy[nod][j])
#		print(" ")

def plotit(start, end, n, sty):
	x = np.arange(start, end, n)
	
	line = plt.plot(x, sty)
	setp(line, linewidth=.3, color='r')
	
	x2 = np.arange(1.34, 1.38501, 0.00001)
	y2 = final_f(x2)
	line2 = plt.plot(x2, y2, tx, final_f(tx), "b.")
	setp(line2, linewidth=.3, color='b')
	
	x3 = np.arange(1.34, 1.38501, 0.00001)
	y3 = reverse_f(x3)
	line2 = plt.plot(x3,y3, tx, reverse_f(tx), "y.")
	setp(line2, linewidth=.3, color='y')
	
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
	
def rev_part(x, i):
	p=dy[i][8-i]
	for j in range(i+1):
		p *= x-stx[9-j]
	return p
	
def reverse_f(x):
	
	fnl = sty[9]
	for i in range(9):
		fnl = fnl + rev_part(x, i)
	return fnl


start, end, n = 1.340, 1.390, 0.005

	
plotit(start, end, n, sty)


print(round(final_f(1.3473),5))
print(round(reverse_f(1.3473),5))

print(round(final_f(1.3763),5))
print(round(reverse_f(1.3763),5))

print(round(final_f(1.3583),5))
print(round(reverse_f(1.3583),5))

print(round(final_f(1.3812),5))
print(round(reverse_f(1.3812),5))

print(round(final_f(1.3787),5))
print(round(reverse_f(1.3787),5))

print(round(final_f(1.3455),5))
print(round(reverse_f(1.3455),5))

print("---------------------------------------")


for i in range(5000):
	x2.append(1.34+i*0.00001)
	y2.append(final_f(1.34+i*0.00001))

intt = 200
print(final_f(1.34+intt*0.00001))
print(y2[200])
