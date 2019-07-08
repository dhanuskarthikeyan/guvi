nc=int(raw_input())
c=0
for i in range(0,nc):
    s=raw_input()
    if(sorted(s)==sorted("kabali")):
        c=c+1
print(c)
