n=input()
co=0
for i in n:
  if n[i].isalpha() or n[i].isdigit() or n[i]==' ':
    continue
  else:
    co=co+1  
print(co)
