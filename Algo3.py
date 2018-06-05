from random import randint 
import time
import sys 
import numpy as np
import matplotlib.pyplot as plt
import copy 
import string
import random

def maximum(x):
	max = 0
	for i in range(len(x)):
		if max < x[i] :
			max = x[i]
	return max
def createArray(n,k):
	a = [[0 for rweq in range(n)] for wqer in range(k)]
	return a
def refillArray(a,n,k):
	for i in range(k):
		a[i][0] = randint(2, k*n*2)
	for i in range(k):
		for j in range(n):
			a[i][j] = randint(a[i][j-1]+2, k*n*2+a[i][j-1]+2)
			#print(i,' ',j,' ',a[i][j],' ', a[i][j-1],' ',k*n*2+a[i][j-1])
	return a

def merge(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        #print(a[0], ' ', b[0],)
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
        #print(c)
    #print(a, ' ', b)
    if len(a) == 0:
        c += b
    else:
        c += a
    #print(c)
    return c

def mergeAll(x):
	x.append([])
	for part in range(0, len(x)-1):
		x[-1]=merge(x[-1], x[part])
	return x[-1]


def mergeDAC(x):
	a = []
	b = []
	#print("y = ", x)
	for part in range(len(x)):
		if (part<len(x)/2):
			a.append(x[part])
		else:
			b.append(x[part])
	
	if (len(a)!=1 and len(a)!=0):
		a=mergeDAC(a)
	else: a=a[0]
	if (len(b)!=1 and len(b)!=0):
		b=mergeDAC(b)
	else: b=b[0]
	#print(a, ' ', b)
	#print("")
	x=merge(a,b)
	return x

	
def mergeLang(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        #print(a[0], ' ', b[0],)
        if tuple(map(ord, a[0])) < tuple(map(ord, b[0])):
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
        #print(c)
    #print(a, ' ', b)
    if len(a) == 0:
        c += b
    else:
        c += a
    #print(c)
    return c

def mergeLangAll(x):
	x.append([])
	for part in range(0, len(x)-1):
		x[-1]=mergeLang(x[-1], x[part])
	return x[-1]

def randomWord(length,r):
	letters = string.ascii_lowercase
	x = letters[r]
	#print('x=', x)
	for i in range(length):
		x = x + random.choice(letters) 
	#print('x=', x)
	return x

def compareString(a,b):
	for i in range(max(len(a), len(b))):
		if (tuple(map(ord, a[i]))<tuple(map(ord, b[i]))):
			return -1
		elif (tuple(map(ord, a[i]))>tuple(map(ord, b[i]))):
			return 1
	return 0

def randomWordArray(l,n,k):
	a = [[randomWord(l,rweq) for rweq in range(n)] for wqer in range(k)]
	return a
	
def countKeysEqual(A,n,m):
	equal = [0 for rweq in range(m+1)]
	for i in range(0,n):
		equal[A[i]] += 1
	#print(equal)
	return equal
def countKeysLess(A,n,m):
	equal = countKeysEqual(A,n,m)
	less = [0 for rweq in range(m+1)]
	for i in range(1,m+1):
		less[i] = less[i-1] + equal[i]
	#print(less)
	return less
def rearrange(A,n,m):
	less = countKeysLess(A,n,m)
	b = [0 for rweq in range(n)]
	next = [0 for rweq in range(m)]
	for i in range(m):
		next[i] = less[i] + 1
	#print(next)
	for i in range(n):
		key = A[i]
		
		index = next[key-1]-1
		#print(index, '/', len(b)-1)
		b[index] = A[i]
		next[key-1] += 1
	return b
def shuffle(a):
	for i in range(len(a)):
		q = randint(i,len(a)-1)
		t = a[i]
		a[i] = a[q]
		a[q] = t

n=4
k=5
a = createArray(n,k)
a = refillArray(a,n,k)
print(a)
a = mergeAll(a)
print(a)
print(' ')
print(' ')
b = createArray(n,k)
b = refillArray(b,n,k)
print(b)
b = mergeDAC(b)
print(b)
print(' ')
print(' ')
c = randomWordArray(3,n,k)
print(c)
c = mergeLangAll(c)
print(c)
print(' ')
print(' ')
d = [0 for rweq in range(n)]
for i in range(n):
	if i == 0 : 
		d[i] = randint(2, 12345)
	else :
		d[i] = randint(2+d[i-1],12345+d[i-1])
	max = d[-1]
		

shuffle(d) 
print(d)
d = rearrange(d,len(d),max)
print(d)
