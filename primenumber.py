def is_prime(n):
	for i in range(1,n+1):
		count = 0
		for j in range(1,i+1):
			if i % j == 0:
				count = count+1
		if count == 2:
			return True
	return False
n = int(input())
print(is_prime(n))
