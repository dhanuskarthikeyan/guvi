def arms(num):
  sum = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  if num == sum:
    print(num)
num1,num2 = raw_input().split()
num1=int(num1)
num2=int(num2)
for i in range(num1,num2):
  arms(i)
