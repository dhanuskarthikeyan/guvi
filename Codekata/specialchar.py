n=raw_input()
co=0
for i in range(0,len(n)):
  if n[i].isalpha() or n[i].isdigit() or n[i]==' ':
    continue
  else:
    co=co+1  
print(co)
