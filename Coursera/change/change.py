# Uses python3
import sys

def get_change(n):
	ten = n//10
	leftover = n%10
	fives =  leftover//5
	leftover =  leftover%5
	ones = leftover
	n = int(ten + fives + ones)
	return n

if __name__ == '__main__':
	n = int(input())
	print(get_change(n))
