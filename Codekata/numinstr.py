s2 = raw_input()
s1 = ""
for i in range(len(s2)):
  if s2[i].isdigit():
    s1 += s2[i]
print s1
