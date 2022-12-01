#!/usr/bin/env python
# coding: utf-8

# In[2]:


# this is design for direct use
def display(li):
    for i in range(3):
        for j in range(3):
            print(li[i][j], end = ' ')
        print()


# In[3]:


# this is design for direct use
def enter_value(value, position ,li):
    n = 0
    for i in range(3):
        for j in range(3):
            n += 1
            if n == position:
                li[i][j] = value


# In[4]:


# this is design for win_processing
def row_checker(li):
    
    global p
    
    li1 = []
    for i in range(3):
        
        p = win_checker(li1)
        if p == 'win':
            break
        
        li1 = []
        for j in range(3):
            li1.append(li[i][j])


# In[5]:


# this is design for win_processing
def col_checker(li):
    
    global p

    li1 = []
    for i in range(3):
        
        p = win_checker(li1)
        if p == 'win':
            break
        
        li1 = []
        for j in range(3):
            li1.append(li[j][i])


# In[6]:


# this is design for win_processing
def dig1_checker(li):
    
    global p
    
    li1 = []
    for i in range(3):
        li1.append(li[i][i])
    
    p = win_checker(li1)


# In[7]:


# this is design for win_processing
def dig2_checker(li):
    
    global p
    
    li1 = []
    for i in range(3):
        for j in range(3):
            if i+j == 2:
                li1.append(li[i][j])
    
    p = win_checker(li1)


# In[8]:


# this is design for row checker , col checker ,etc
def win_checker(li1):
        if li1 == ['x','x','x']:
            print('x  WIN')
            return 'win'
        elif li1 == ['o','o','o']:
            print('o  WIN')
            return 'win'
        else:
            return 'continue'
            


# In[9]:


# this is design for direct use
def win_processing(li):
    
    row_checker(li)
    if p == 'win':
        return
    
    col_checker(li)
    if p == 'win':
        return
    
    dig1_checker(li)
    if p == 'win':
        return
    
    dig2_checker(li)
    if p == 'win':
        return
    
    print('continue')


# In[10]:


# this is design for direct use
def new_game():
    global li
    global p
    p = 'none'
    li = []
    for i in range(3):
        li1 = []
        for j in range(3):
            li1.append('0')
        li.append(li1)
    return li


# In[13]:


print('TIC-TAC-TOE')
new_game()
display(li)
while p != 'win':
    n = input('''Type the value and position
    For example, x 6   or   o 9
    positions are like
    1  2  3
    4  5  6
    7  8  9    :''').split()
    value = n[0]
    position = int(n[1])
    enter_value(value,position,li)
    display(li)
    win_processing(li)

