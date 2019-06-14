n1, n2= map(int,raw_input().split())
while n1 != n2:
  if n1>n2:
    n1 = n1 - n2
  else:
    n2 = n2 - n1
if n1 == 0:
  print n2
else:
  print n1
