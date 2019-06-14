import math
nn,m5=map(int,raw_input().split())
k=(nn*m5)
q=int(math.sqrt(k))
if(k==q*q):
	print("yes")
else:
	print("no")
