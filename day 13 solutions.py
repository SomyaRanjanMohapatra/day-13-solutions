#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
def maxPrimeFactors (n): 
      
    # Initialize the maximum prime factor 
    # variable with the lowest one 
    maxPrime = -1
    for n in range(1,1016):
        while n % 2 == 0: 
            maxPrime = 2
            n >>= 1     # equivalent to n /= 2 
          
    # n must be odd at this point,  
    # thus skip the even numbers and  
    # iterate only for odd integers 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
      
    # This condition is to handle the  
    # case when n is a prime number  
    # greater than 2 
    if n > 2: 
        maxPrime = n 
      
    return int(maxPrime) 
  
# Driver code to test above function 
n =54
print(maxPrimeFactors(n)) 
  


# In[ ]:




