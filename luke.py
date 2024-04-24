#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys


# In[ ]:


family = {'Darth Vader' : 'father', 'Leia' : 'sister', 'Han' : 'brother in law', 'R2D2' : 'droid', 'Rey' : 'Padawan', 'Tatoonie' :'homeworld'}


# In[ ]:


def relations():
    name = sys.argv[1]
    if name == 'Darth Vader':
        print(f'No, I am your {family[name]}')
    else:
        print(f'Luke, I am your {family[name]}')
        
    
relations()

