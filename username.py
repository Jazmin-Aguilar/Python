#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys    


# In[ ]:


def username():
    full_name = sys.argv[1:]
    initial = full_name[0][0].lower()
    last_name = full_name[-1][-7:].lower()
    number = "".join(full_name)
    print(f'Your username is {initial}{last_name}{len(number)}')


# In[ ]:


username()

