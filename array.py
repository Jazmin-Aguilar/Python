#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys


# In[ ]:


import numpy as np


# In[ ]:


x = np.array([int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])])
print(type(x))


# In[ ]:


y = int(sys.argv[1])*int(sys.argv[2])*int(sys.argv[3])*int(sys.argv[4])
print(y)

