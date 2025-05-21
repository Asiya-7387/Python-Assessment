# find common elements in two lists

# Problem 1: Given two lists, return a set of elements common to both.
#Input: [1, 2, 3, 4] and [3, 4, 5, 6]
#Output: {3, 4}


# l1=[1,2,3,4]
# l2=[3,4,5,6]

# s1=set(l1) # convert list to set

# s2=set(l2) # convert list to set

# print(s1)

# print(s2)


# s3=s1.intersection(s2)

# print(s3)
#----------------------------------------------------------

# Unique Vowels in a Word
#  Problem 2: Write a function that returns the number of unique vowels in a word.
# Input: "education"
# Output: 5

# def count_unique_vowels(word):
#      word="education"
#      vowels="aeiouAEIOU"
#      unique_vowels=set()
#      for char in  word:
#          if char in vowels:
#              unique_vowels.add(char)
#      return len(unique_vowels)
# word="education" 
# result=count_unique_vowels(word) 
# print(result)

#------------------------------------------------------------
# Check Subset
# Problem 3: Check if one set is a subset of another.
 # Input: A = {1, 2, 3}, B = {1, 2}
# Output: True

# A={1,2,3}
# B={1,2}

# print(B.issubset(A))

#---------------------------------------------------------

#Find Missing Elements
#Problem 4: Given two lists of integers where one is a subset of the other 
#(with some elements missing), find the missing elements using sets.
#Input: original = [1, 2, 3, 4, 5], received = [2, 3, 5]
#Output: {1, 4}


# l1=[1,2,3,4]

# s1=set(l1)

# print(s1)

# l2=[2,3,5]

# s2=set(l2)

# print(s2)


# s3=s1.difference(s2)

# print(s3)

#------------------------------------------------------


#Count Unique Words in a Paragraph

#Problem  5: Write a function that returns the number of unique words in a paragraph.
#Input: "This is a test. This test is easy."
#Output: 5 ({'this', 'is', 'a', 'test', 'easy'})


def count_unique_words(paragraph):  # this function counts the no.of unique words in a given paragraph

       text=paragraph.lower()     #convert input string to lowecase
       
       text=text.replace(".","").replace(",","")   # remove punctuation using replace method
    
       words=text.split() # split the string into a list words using split() method
    
       unique_words=set(words)  # # create empty set to store unique words.iterate through the list of words & add each word to the set
    #set only store unique element,duplicate element will be ignored
                                   
       return len(unique_words),unique_words
                                         

paragraph1 = "this is a test. this test is easy."
count,unique_set=count_unique_words(paragraph1)

print(f"Output:{count} ({unique_set})")










