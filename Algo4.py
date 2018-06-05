from time import clock
from numpy import arange, random
from pylab import plot, grid, legend, show


def insertionsort(A):
	for j in range(1,len(A)):
		key = A[j]
		i = j-1 
		while (i > -1) and key < A[i]: 
			A[i+1]=A[i] 
			i=i-1
			A[i+1] = key
	return A
	
def merge(left, right):
	result = list()
	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			result.append(left[0])
			del left[0]
		else:
			result.append(right[0])
			del right[0]
	if len(left) != 0:
		result = result + left
	elif len(right) != 0:
		result = result + right
	return result

def count_keys_equal(arr, mrange):
	result = list()
	for x in range(0, mrange):
		result.append(0)
	for x in range(0, len(arr)):
		key = arr[x]
		result[key] = result[key] + 1
	return result
		
def count_keys_less(equal, mrange):
	result = list()
	for x in range(0, mrange):
		result.append(0)
	for x in range(1, mrange):
		result[x] = result[x - 1] + equal[x - 1]
	return result
		
def rearrange(arr, less, mrange):
	next = list()
	result = list()
	for x in range(0, len(arr)):
		result.append(0)
	for x in range(0, mrange):
		next.append(0)
	for x in range(0, mrange):
		next[x] = less[x] + 1
	for x in range(0, len(arr)):
		key = arr[x]
		index = next[key] - 1
		result[index] = arr[x]
		next[key] = next[key] + 1
	return result
	
def merge_sort(arr):
	if(len(arr) <= 1):
		return arr
	else:
		mid = int(len(arr) / 2)
		left = list()
		for x in arr[0 : mid]:
			left.append(x)
		right = list()
		for x in arr[mid : len(arr)]:
			right.append(x)
		left = merge_sort(left)
		right = merge_sort(right)
		result = merge(left, right)
		return result

def counting_sort(arr, mrange):
	equal = count_keys_equal(arr, mrange + 1)
	less = count_keys_less(equal, mrange + 1)
	result = rearrange(arr, less, mrange + 1)
	return result

def selection_sort(arr):
	for x in range(0, len(arr) - 1):
		smallest = x
		for y in range(x + 1, len(arr)):
			if arr[y] < arr[smallest]:
				smallest = y
		arr[x], arr[smallest] = arr[smallest], arr[x]
	return arr

Y1 = [0.17229799999999995, 0.2364240000000002, 0.2480139999999995, 0.33250400000000013, 0.4180869999999999, 0.49876700000000085, 0.5296909999999997, 0.5992109999999968, 0.6583499999999987, 0.7465740000000096, 0.7760560000000112, 0.8634079999999926, 0.9335920000000328, 1.0240740000000415, 1.018105000000105, 1.0949080000000322, 1.131010999999944, 1.1997659999999541, 1.4033509999999296, 1.3643899999999576]           
Y2 = [1.295299, 3.3868919999999996, 6.537977000000001, 10.491477999999999, 15.661825, 21.306514, 28.90925, 35.93050199999999, 44.90814999999999, 58.614069, 69.44128500000002, 82.28116899999998, 93.44221300000004, 109.29741099999995, 126.48598300000003, 143.01465200000007, 163.94232999999997, 185.35701799999993, 204.34829100000002, 222.64737999999988]
X = arange(50000, 1050000, 50000)
"""
k  = 50000
for x in range(0, 10):
	A = random.randint(0, 100000, k * (x + 1)).tolist()
	
	start_time = clock()
	counting_sort(A, 100000)
	t = clock() - start_time
	Y1.append(t)
	
	start_time = clock()
	merge_sort(A)
	t = clock() - start_time
	Y2.append(t)
print(Y1, '         ', Y2)
"""
line_counting_sort = plot(X, Y1, label = "Counting sort")	
line_merge_sort = plot(X, Y2, label = "Merge_sort")
plot(X, Y1, 'r.', X, Y2, 'r*')
grid()
legend()
show()	
	
	
x = [32,34,2,5,23,32,73,24,54,73,37]