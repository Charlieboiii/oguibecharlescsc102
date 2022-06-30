#!/usr/bin/env python
# coding: utf-8

# In[1]:


count=[10,20,30,40,50]
for num in count:
    print(num)


# In[ ]:


num =0 
for num in range(6):
    num=num + 1
    if num == 3:
        continue
    print('num has a value' + str(num))
print('end of loop')


# In[ ]:


for num in range(5):
    if num>0:
        print(num * 10)


# In[ ]:


count = 1
while count <=5:
    print(count)
         count +=1


# In[ ]:




