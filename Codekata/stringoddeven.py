m=raw_input()
j,l="",""
for i in range(0,len(m)):
  if(i%2==0):
    j+=m[i]
  else:
    l+=m[i]
print j,l
