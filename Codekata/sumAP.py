a, d, N = map(int,raw_input().split())
sum = 0
for i in range(1,N+1):
  sum += a+(i-1)*d
print sum
