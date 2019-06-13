string=list(map(int,raw_input()))

for i in range(len(string)):
  if(string[i]==0 or string[i]==1):
    continue
  else:
    break
if(i+1==len(string)):
  print("yes")
else:
  print("no")
