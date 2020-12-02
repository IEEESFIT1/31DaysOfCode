#!/usr/bin/env python
# coding: utf-8

# In[12]:


import random

while True:
    try:
        length=int(input('Enter the length of password(min:8/max:20):'))
    except:
        print('Enter an integer value!!')
    else:
        if length<8 or length>20:
            continue
        else:
            break
lower_case=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
upper_case=[]
password=''
for letter in lower_case:
    upper_case.append(letter.upper())


# In[13]:


numbers=['0','1','2','3','4','5','6','7','8','9',]

special_characters=['!','@','#','$','%','^','&','*','-','_','/','?']

random.shuffle(lower_case)
random.shuffle(upper_case)
random.shuffle(numbers)
random.shuffle(special_characters)


# In[14]:


password+=random.choice(lower_case)+random.choice(upper_case)+random.choice(numbers)+random.choice(special_characters)+random.choice(upper_case)+random.choice(lower_case)+random.choice(special_characters)+random.choice(numbers)


# In[15]:


for n in range(length-8):
    password+=random.choice(lower_case)


# In[ ]:





# In[16]:


password


# In[17]:


temp_pass=list(password)


# In[18]:


random.shuffle(temp_pass)


# In[19]:


temp_pass


# In[20]:


final_password=''
#passw=final_password.join(temp_pass)
for char in temp_pass:
    final_password+=char


# In[21]:


final_password


# In[22]:


print(f"The password is:{final_password}")


# In[ ]:





# In[ ]:




