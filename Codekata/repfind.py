a,b=(raw_input().split())
a=int(a)
b=int(b)
temp=list(map(int,raw_input().split()))
if temp.count(b) > 0:
  print("yes")
else:
  print("no")
