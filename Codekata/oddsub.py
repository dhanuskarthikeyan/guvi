num,n=(raw_input().split())
num=int(num)
n=int(n)
num=abs(n-num)
if(num>=0):
  if(num%2==0):
    print "even"
  else:
    print "odd"
else:
  print "invalid"
