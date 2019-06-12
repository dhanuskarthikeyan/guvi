lw,up=raw_input().split()
lower=int(lw)
upper=int(up)
for num in range(lower,upper):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print num,
