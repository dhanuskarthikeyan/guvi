num,n=(raw_input().split())
num=int(num)
n=int(n)
num=n+num
if(num>=0):
  if(num%2==0):
    print "Even"
  else:
    print "Odd"
else:
  print "invalid"
