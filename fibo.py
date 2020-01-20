def fibo(n):
	if n==0:
		print("Digit should be greater than 0.")
	elif n==1:
		return 0	
	elif n==2: 
		return 1
	else: 
		return fibo(n-1)+fibo(n-2)

n = int(input("Enter the digit upto which you want to find fibnacci series: "))


l = list()
l=[str(fibo(i)) for i in range(1,n+1)]
s = ",".join(l)
print(s)