# Uses python3
import random

def max_fix(a):
	result = 0
	max = 0
	second = 0
	index = 0
	for i in range(0, n):
		if a[i]  > max:
			max = a[i]
			index = i

	a[index] = 0
	
	for i in range(0,n):
		if a[i] > second:
			second = a[i]

	result = max * second

	print(result)



def max(a):
	result = 0

	for i in range(0, n):
		for j in range(i+1, n):
			if a[i]*a[j] > result:
				result = a[i]*a[j]

	print(result)


'''
	
while(True):
	n = random.randint(2, 100)
	print(n, "\n")
	a = list()
	for i in range(0, n):
		a.append(random.randint(1,10000000))
		print(a[i], " ", end = "")
		
	print("")
	ans1 =  max_fix(a)
	ans2 =  max(a)
	
	if(ans1 != ans2):
		print("wrong answer, Max is ", ans2, " Max_fix is ", ans1)
		break
	else:
		print("OK")

'''		

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)
max_fix(a)


