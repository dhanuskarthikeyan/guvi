a1=list(raw_input())
if len(a1)%2==0:
    a1[int(len(a1)/2)] ='*'
    a1[int(len(a1)/2)-1]='*'
else:
    a1[int(len(a1)/2)] ='*'
print ''.join(str(i) for i in a1)
