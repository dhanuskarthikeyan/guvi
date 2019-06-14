st= raw_input()
f = 0
for i in range(len(st)):
  if st.count(st[i]) != 1:
    f = 1
if f == 0:
  print "Yes"
else:
  print "No"
