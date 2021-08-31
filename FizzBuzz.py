#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = int(input())

for num in range(0,num):

  if num % 2 == 0:
    continue
  elif num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 3 == 0:
    print('Fizz')
  elif num % 5 == 0:
    print('Buzz')
  else:
    print(num)

    


# In[ ]:




