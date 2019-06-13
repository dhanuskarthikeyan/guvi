n=raw_input()
co=0
ko=0
for i in range(0,len(n)):
  if n[i].isalpha():
    co=co+1
  elif n[i].isdigit():
    ko=ko+1  
  else:
    continue
if ko>=1 and co>=1:
  print "yes"
else :
  print "no"
