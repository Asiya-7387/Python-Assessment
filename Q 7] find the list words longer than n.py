# Q 7]. Write a Python program to find the list of words that are longer than given words

n=4    # MINIMUM length of word 

str="Find the List of Words that are Longer than n from a given List of Words"

new_list = []

text = str.split(" ") # split()- to separate the string into a list of words.

for x in text:   #biterate through each word in the list
    
	if len(x) > n: # check if the length of the word is greater than n
        
		new_list.append(x) # add the word in new_list
        
print(new_list)



# o/p-->['Words', 'Longer', 'given', 'Words']