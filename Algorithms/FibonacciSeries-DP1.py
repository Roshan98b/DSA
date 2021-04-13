# Fibonacci Series using Dynamic Programming
def fibonacci(n):
	
	# Taking 1st two fibonacci nubers as 0 and 1
	f = [0, 1]
	
	
	for i in range(2, n+1):
		f.append(f[i-1] + f[i-2])
	return (f)

# Main function
if __name__ == "__main__":
	print(fibonacci(5))
