#!/usr/bin/env python
# coding: utf-8

# In[1]:


import this


# In[5]:


x=5
y=8
message="Hello Python"
print(message)


# In[6]:


message="Hello Python"
print(message)


# In[7]:


name="srinivas"
print(name.title())


# In[9]:


print(name.upper())


# In[10]:


print(name.lower())


# In[16]:


firstname="srinivas"
lastname="madasu"
fullname=f"{firstname}{lastname}"
print(fullname)
print(fullname.title())
print(fullname.upper())
print(fullname.lower())


# In[26]:


print("\t\tpython")
print("languages :\nPython\nc\nJava")


# In[2]:


x="values is"
x="values"
print(x)


# In[30]:


x="value  "
x="value"
print(x)
print(x.strip())


# In[35]:


# operators
2+3,5-4,5*5,5%5


# In[32]:


x,y,z=1,2,3


# In[80]:


bicycles=['car','bus','cycle','flight']
print(bicycles[0])
print(bicycles[3])
print(bicycles[1])
print(bicycles[2])
print(bicycles[0].title())
# Assign a new value
bicycles[2]='helicopter'
print(bicycles)
# Apend a value
bicycles.append('ranger')
print(bicycles)
# Insert a new value
bicycles.insert(5,'acter')
print(bicycles)
# Delete a value
bicycles.pop(5)
print(bicycles)
# Sort a new value
bicycles.sort()
print(bicycles)
bicycles.reverse()
print(bicycles)


# In[81]:


bikes=[]
print("initial blank list")
print("bikes")


# In[49]:


motorcycles=['honda','yamaha','suziki']
print(motorcycles[-1])


# In[50]:


students=['pankaj','manoj','rambabu']
for student in students:
    print(student)


# In[55]:


students=['pankaj','manoj','rambabu']
for student in students:
    print(f"{student.title()},you are best")
print("Thankyou")


# In[62]:


numbers=list(range(1,9))
print (numbers)


# In[63]:


for value in range(1,11):
    print(value)


# In[73]:


square=[]
for value in range(1,16):
    square=value ** 2
    squares.append(square)
    print(square)


# In[89]:


#Sclicing of List

Players=['Kohli','Dhoni','Yuvi','Sachin']
print(Players[0:3])
print(Players[2:5])
print(Players[:2])
print(Players[0:])
print('Captain of india team')
for player in Players[:2]:
    print(player.title())


# In[91]:


#Coping a List
my_food=['rice','curry','dosa','idly','veg','non-veg']
friends_food=my_food[:]
print(friends_food)
my_food.append('choclate')
friends_food.append('ice cream')
print(my_food)
print(friends_food)


# In[79]:


squares=[]
for value in range(1,16):
    square=value ** 2
    squares.append(square)
    print(squares)


# In[ ]:





# In[ ]:




