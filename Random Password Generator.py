#!/usr/bin/env python
# coding: utf-8

# # To create a program that takes a number and generate a random password length of that number.

# In[1]:


import random

passlen = int(input("enter the length of password"))
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIKJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
generated_pwd = "".join(random.sample(s, passlen))
print(generated_pwd)

