n,k=(raw_input().split())
n=int(n)
k=int(k)
a=[]
for x in raw_input().split():
  a.append(int(x))
b=a[:k]
print sum(b)
