n=raw_input()
co=0
for i in range(0,len(n)):
  if n[i].isalpha() or n[i].isdigit() or n[i]==' ' or n[i]==".":
    continue
  else:
    break
if i==len(n)-1 :
  print "Yes"
else :
  print "No"
