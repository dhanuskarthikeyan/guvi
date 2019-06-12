a=int(input())
ba=[]
for x in raw_input().split():
  ba.append(int(x))
ba.sort()
length = len(ba)
if (length % 2 == 0):
    median = (ba[(length)//2] + ba[(length)//2-1]) / 2
else:
    median = ba[(length-1)//2]
print(median)
