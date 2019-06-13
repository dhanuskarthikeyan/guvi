import math 
def check(n): 
    if n == 1: 
        return False
    for x in range(2, (int)(math.sqrt(n))+1): 
        if n % x == 0: 
            return False 
    return True
n3 = int(input())
if check(n3): 
    print("yes")  
else: 
    print("no") 
