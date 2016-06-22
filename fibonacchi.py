n = int(input())


def fibrecur(n):
	
	if n <= 1:
		return n

	else:
		return fibrecur(n-1) + fibrecur(n-2) 

def fibarray(n):
	
	a =  [None] * (n+1)
	a[0] = 0
	a[1] = 1


	for i in range(2, n+1):
		a[i] =  a[i-1] + a[i-2]
		#print(a)
	return a[n]
		
print(fibrecur(n))
print(fibarray(n))