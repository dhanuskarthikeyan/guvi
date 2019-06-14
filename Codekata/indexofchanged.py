n = int(raw_input())
l = map(int,raw_input().split())
for i in range(len(l)-1):
  if l[i] > l[i+1]:
    print i
    break
