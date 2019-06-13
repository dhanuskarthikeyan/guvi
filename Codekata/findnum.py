a1=int(raw_input())
a2,a3=raw_input().split()
a2=int(a2)
a3=int(a3)
for a in range(a2,a3):
  if(a==a1):
    co=1
if(co==1):
  print"yes"
else:
  print "no"
