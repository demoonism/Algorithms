best = 0
a = [int(x) for x in input().split()]
#print(a[0], " - ",a[1])
for i in range(1, a[0] +a[1]):
	if a[0] % i == 0 and a[1] % i == 0:
		best = i
print(best)