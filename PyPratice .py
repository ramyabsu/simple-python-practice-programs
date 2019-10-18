#!/usr/bin/env python
# coding: utf-8

# # Python practice
# Write a Python program to calculate the length of a string

# In[6]:


len('Hello there')


# In[7]:


mystr = "Hello there"
length = 0
for i in mystr:
    length +=1
length


# #Write a Python program to sum all the items in a list.

# In[14]:


#Write a Python program to sum all the items in a list.
my_list = [1, 2, 3, 4 ,5]
total = 0
for i in my_list:
    total += i
total
    


# In[16]:


#Write a Python program to get the largest number from a list

my_list = [2, 4, 1, 7, 3]
largest = 0
for i in my_list:
    if i > largest:
        largest = i
largest


# In[22]:


#Write a Python program to count the number of characters (character frequency) in a string

mystr = "jdaksdjalks slkjsk"
mydict = {}
for i in mystr:
    key = mydict.keys()
    if i == ' ':
        pass
    else:
        if i in key:
            mydict[i] += 1    
        else:
            mydict[i] = 1
    
mydict

        


# In[48]:


#Write a Python program to count the number of strings where the string length is 2
#or more and the first and last character are same from a given list of strings.

words = ['abc', 'abcd', 'abcde', 'aba']
count = 0
for word in words:
    if len(word) > 1 and word[0]==word[-1]: 
        count += 1
count


# In[65]:


#Write a Python program to get a list, sorted in increasing order by 
#the last element in each tuple from a given list of non-empty tuples

mylist = [(2, 5, 1), (1, 2), (4, 4), (2, 3), (2, 0)]
sorted_list = sorted(mylist, key=last)
sorted_list


# In[82]:


#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
#If the string length is less than 2, return instead the empty string

mystr = "python"
if len(mystr)<2:
    print('')
else:
    first2 = mystr[:2]
    last2 = mystr[-2:]
    finalstr= first2 + last2
    print(finalstr)


# In[109]:


#Write a Python program to get a string from a given string where all occurrences of its 
#first char have been changed to '$', except the first char itself.

mystr = "ramyashreerr"
mylist = list(mystr)
finalstr = ''
for i in range(1,len(mylist)):    
    if mylist[i] ==  mylist[0]:       
        mylist[i] = '$'       
finalstr = finalstr.join(mylist)
print(finalstr)

#or 

def change_char(str1):  
  char = str1[0]  
  #length = len(str1)  
  str1 = str1.replace(char, '$')  
  str1 = char + str1[1:]  
  
  return str1  
  
print(change_char('ramyashree')) 
    


# In[111]:


#Write a Python program to get a single string from two given strings, 
#separated by a space and swap the first two characters of each stringdef chars_mix_up(a, b):  

str1 = 'abc'
str2 = 'xyz'
new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]  
  
print(new_str1 + " " + new_str2)


# In[130]:


#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
#If the given string is already ends with 'ing' then add 'ly' instead. 
#If the string length of the given string is less than 3, leave it unchanged.
mystr = "perfect"
if len(mystr) < 3:
    pass
else:
    if mystr[-3:] == 'ing':        
        mystr = mystr + 'ly'
    else:
        mystr = mystr + 'ing'    
mystr


# In[138]:


#find the longest word in the list of words
words_list = ["Java", 'Csharp', 'Javascript', 'Jquery', 'HTML', 'Python', 'CSS']
word_len = []
for n in words_list:
    word_len.append((len(n), n))
word_len.sort()
print(word_len)
word_len[-1][1]


# In[11]:


#Write a Python program to test whether an input is an integer
user_input = input('Enter an integer or a string: ')
try:
    user_input= int(user_input)  
    print('The input is an interger')  
except ValueError:  
    print('The input is a string')
    


# In[60]:


#Write a Python program to sort (ascending and descending) a dictionary by key
mydict = {3: 4, 2: 1, 4: 3, 0: 0, 1: 2, 6:1, 5:5}
#without operator/ by converting dict to list
mylist = list(mydict.items())
print(mylist)
sorted_list = sorted(mylist)
#or
#sorted_list = sorted(mylist, key=lambda x:x[0]) 
#both the above lines gives the same output
sorted_dict = dict(sorted_list)
print('Dictionary in Ascending order by key:', sorted_dict)
sorted_list = sorted(sorted_list, reverse=True)
sorted_dict = dict(sorted_list)
print('Dictionary in Descending order by key:', sorted_dict)

#using operator
import operator

sorted_list_asc = sorted(mydict.items(), key=operator.itemgetter(0))
sorted_dict_asc =dict(sorted_list_asc)
print('Dictionary in Ascending order by key: ',sorted_dict_asc)
sorted_desc = dict( sorted(mydict.items(), key=operator.itemgetter(0),reverse=True))
print('Dictionary in Descending order by key: ',sorted_desc)


# In[59]:


#Write a Python program to sort (ascending and descending) a dictionary by value.
mydict = {3: 4, 2: 1, 4: 3, 0: 0, 1: 2, 6:1, 5:5}
#without operator

sorted_dict = sorted(mydict.items(), key=lambda x: x[1])
print('Ascending order by value using lambda function: ', dict(sorted_dict))
sorted_dict = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
print('Decending order by value using lambda function: ', dict(sorted_dict))
print('----------------------------------')
import operator

sorted_asc = dict(sorted(mydict.items(), key=operator.itemgetter(1)))
print('Ascending order by value using operator module : ',sorted_asc)
sorted_desc = dict( sorted(mydict.items(), key=operator.itemgetter(1),reverse=True))
print('Descending order by value using operator module: ',sorted_desc)


# In[9]:


#Write a Python program to add key to a dictionary

mydict = {'Name':'Ramya', 'ID': 123,}
print(mydict)
mydict.update({'Email':'ramya@gmail.com'})
print(mydict)


# In[11]:


#Write a Python program to concatenate dictionaries to create a new one
dict1 = {'Name':'Ramya', 'ID': 123,}
dict2 = {'Email':'ramya@gmail.com'}
dict3 = {'phNumber': 1234553223}
dict4 = {}

for d in (dict1, dict2, dict3): 
    dict4.update(d)
print(dict4)


# In[19]:


#Write a Python program to check if a given key already exists in a dictionary
mydict = {'Name': 'Ramya', 'ID': 123, 'Email': 'ramya@gmail.com', 'phNumber': 1234553223}
def search_key(k):
    if k in mydict:
        print('key already present')
    else:
        print('Key does not present')
search_key('ID')
search_key('Address')


# In[32]:


#Write a Python program to iterate over dictionaries using for loops
mydict = {'Name': 'Ramya', 'ID': 123, 'Email': 'ramya@gmail.com', 'phNumber': 1234553223}
for i in mydict:
    print(i)
for k, v in mydict.items():
    print(k, ":", v)


# In[62]:


#Write a Python program to remove duplicates from a list.

mylist = [1, 3, 4, 6, 6, 3, 1, 4]
myset = set(mylist)
print(list(myset))


# In[69]:


#Write a Python program to check a list is empty or not.

def empty_or_not(l):
    if not l:
        print('The list is empty')
    else:
        print(l)
empty_or_not([])
empty_or_not([1,2])


# In[70]:


#Write a Python program to clone or copy a list.
mylist = [1, 2, 3]
copy_list = mylist.copy()
copy_list


# In[73]:


#Write a Python program to remove the nth index character from a non empty string. 
mystring = 'All ezzzz well!!'
fstr = mystring[:7]
sstr = mystring[8:]
final_str = fstr + sstr
final_str


# In[22]:


#Write a Python program to change a given string to a new string where the first and last chars have been exchanged. 


# In[23]:


#Write a Python program to remove the characters which have odd index values of a given string


# In[24]:


#Write a Python program to find the list of words that are longer than n from a given list of words.


# In[25]:


#Write a Python program to count the occurrences of each word in a given sentence.


# In[ ]:


#Write a Python function that takes two lists and returns True if they have at least one common member.

