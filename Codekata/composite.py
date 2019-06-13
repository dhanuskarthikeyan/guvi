def isComposite(n):  
    if (n <= 1): 
        return False
    if (n <= 3): 
        return False
    if (n % 2 == 0 or n % 3 == 0): 
        return True
    i = 5
    while(i * i <= n): 
          
        if (n % i == 0 or n % (i + 2) == 0): 
            return True
        i = i + 6
          
    return False
a=int(raw_input())
if (isComposite(a)):
  print"yes"
else:
  print"no"
