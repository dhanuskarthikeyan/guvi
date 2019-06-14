s = raw_input()
le = list(s)
s1 = ""
le.sort()
for i in range(len(le)):
  s1 += le[i]
print s1
