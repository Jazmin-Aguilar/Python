#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys


# In[ ]:


def temp():
    Celsuis = float(sys.argv[1])
    x = Celsuis*9/5 +32
    format_x = '{:.2f}'.format(x)
    print(f'The temperature is',format_x,'degrees Fahrenheit.')
temp()

