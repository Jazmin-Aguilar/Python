#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys


# In[ ]:


a = int(sys.argv[1])


# In[ ]:


b = int(sys.argv[2])


# In[ ]:


c = int(sys.argv[3])


# In[ ]:


d = int(sys.argv[4])


# In[ ]:


e = int(sys.argv[5])


# In[ ]:


x = a+b*0.25+c*0.10+d*0.05+e*0.01
x = round(x,2)
#the round 2 function rounds answer to 2 decimal places
print(f'The total value of your change is ${x}')

