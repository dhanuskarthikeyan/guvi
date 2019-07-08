qw=int(raw_input())
ss=list(map(int,raw_input().split()[:qw]))
count=0
for i in range(0,qw+1):
   if(ss.count(i)==1):
      print(i)
