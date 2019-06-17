l,d=map(int,raw_input().split())
a=list(map(int,raw_input().split()))
b=[]
for i in a:
  j=int(i)
  if(j%2!=0):
    b.append(j)
print b[d-1]
