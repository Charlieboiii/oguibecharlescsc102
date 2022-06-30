#!/usr/bin/env python
# coding: utf-8

# In[2]:


def check_genius(n):
    if n in range(3,9):
        print(str(n), " is in the range")
    else:
              print(str(n), " is not in the range")
check_genius(5.1)   
              


# In[4]:


def is_power_of_two(n):
    return n >0 and (n &(n-1))==0
print(is_power_of_two(36))


# In[ ]:




