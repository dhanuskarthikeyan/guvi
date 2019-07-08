n1=raw_input()
n2='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
ny3=''
for i in n1:
  if i in n2:
    a=n2.index(i)
    a=a+3
    ny3=ny3+n2[a]
print(ny3)
