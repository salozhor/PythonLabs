from random import randint 
import time
import sys 
def Task1_linear(x, point):
	answer = "not found"
	for a in range(len(x)):
		if (x[a] == point):
			answer = a
	return a
			
def Task1_binary(x, point, a, b):
	if (a+1==b and x[a]!=point and x[b]!=point): 
		return "Error. Number was not found"
	c = (a + b) / 2 + 0.01
	c = round(c)
	if (x[c]>point): return Task1_binary(x, point, a, c)
	if (x[c]<point): return Task1_binary(x, point, c, b)
	if (x[c]==point): return c

def Task2_binary(x, point, a, b):
	c = (a + b) / 2 + 0.01
	c = round(c)
	if (a+1==b and x[a]!=point and x[b]!=point): 
		return -c-1
	if (x[c]>point): return Task2_binary(x, point, a, c)
	if (x[c]<point): return Task2_binary(x, point, c, b)
	if (x[c]==point): return c

def BetterLinearSearch(x, point):
	for a in range(len(x)):
		if (x[a] == point):
			return a
	return "not found"
			

def timing_Better(x, point):
	time1 = time.time()
	ret = BetterLinearSearch(x, point)
	time2 = time.time()
	print ('Better Linear Search took %0.3f ms' % ((time2-time1)*1000.0))
	return ret
	
def SentinelLinearSearch(x, point):
	n=len(x)-1
	last = x[n]
	x[n] = point
	i=0
	while (x[i]!=point):
		i+=1
	x[len(x)-1] = last

	if (x[i]==point or i==len(x)-1): return i
	return "not found"
			
def timing_Sentinel(x, point):
	time1 = time.time()
	ret = SentinelLinearSearch(x, point)
	time2 = time.time()
	print ('Sentinel Linear Search took %0.3f ms' % ((time2-time1)*1000.0))
	return ret 
	
def RecursiveLinearSearch(x, point, i):
	n= len(x)-1
	if (i>n): return "not found"
	if (x[i]==point): return i
	return RecursiveLinearSearch(x, point, i+1)
	
def timing_Recursive(x, point):
	time1 = time.time()
	ret = RecursiveLinearSearch(x, point, 0)
	time2 = time.time()
	print ('Recursive Linear Search took %0.3f ms' % ((time2-time1)*1000.0))
	return ret

print("Task 1 linear search for 7 in -7,1,3,3,4,7,11,13.")
array1=[-7,1,3,3,4,7,11,13]
print("Result: ", Task1_linear(array1, 7))
print()
print("Task 1 binary search for 8 in -7,2,2,3,4,7,8,11,13.")
array2=[-7,2,2,3,4,7,8,11,13]
print("Result: ", Task1_binary(array2, 8, 0, len(array2)))
print()
print("Task 1 binary search for 8 in -7,1,2,3,5,7,10,13.")
array3=[-7,1,2,3,5,7,10,13]
print("Result: ", Task1_binary(array3, 8, 0, len(array3)))
print()
print("Task 2 binary search for 8 in -7,1,2,3,5,7,10,13.")
print("Result: ", Task2_binary(array3, 8, 0, len(array3)))
print()
print()

x=list(range(500))
point = randint(0, 500)
print("Looking for ", point, " in 0-500")
print(timing_Better(x, point))
print(timing_Sentinel(x, point))
print(timing_Recursive(x, point))
print()
x=list(range(1000))
point = randint(0, 1000)
print("Looking for ", point, " in 0-1000")
print(timing_Better(x, point))
print(timing_Sentinel(x, point))
print(timing_Recursive(x, point))
print()
sys.setrecursionlimit(5010)
x=list(range(5000))
point = 3210
print("Looking for ", point, " in 0-5000")
print(timing_Better(x, point))
print(timing_Sentinel(x, point))
print(timing_Recursive(x, point))