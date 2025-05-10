#s1='hello to all good morning ,welcome to python'
# print(s1)

# s2="It's my first python session"
# print(s2)



# s1="hello to all"
# #python supports for +ve & -ve indexing

# print(s1[6])

# count=0
# for s in s1:
#   if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
#       count+=1
#       print(s)
# print(count)      


#  OR



# vowel='aeiou'
# count=0
# for s in s1:
#     if s not in vowel:
#         count+=1
#         print(s)
        
# print(count)        

# s1="hello to all good morning ,welcome to python"

# print(s1[13:25])# extract substring from the given string(slice)

# print(s1[:25])

# print(s1[4:29:3])

# print(s1[-1:-20:-1])

# print(s1[::-1])#print string in reverse order

# find the given string is palindrome or not

# str1='nitin'

# if str1==str1[::-1]:
#     print('palindrome')

# else:
#     print("not palindrome")
    
 # built in function to work with string
   
s1="    Hello to all Good Morning,Welcome to python"

# print(len(s1))

# print(s1.lower())#show all letters are  in lowercase

# print(s1.upper())# show all letters are in uppercase

# print(id(s1))  # show address location

s1=s1.replace("Hi","Hello")
print(s1)

print(s1.strip()) # all leading & trailing spaces will be removed

s1=s1.strip()

print(s1.startswith("Hi"))


s1="Hello,my age is 25 my id is abc@gmail.com"

#chars,numbers,special charcters

char_count=0
num_count=0
symbol_count=0
space_count=0
for s in s1:
     if s.isalpha():
         char_count+=1
     elif s.isdigit():
         num_count+=10
     elif s.isspace():
         space_count+=1
     else:
         symbol_count+=1
         
print("chars count",char_count) 
print("number count",num_count) 
print("symbol count ",symbol_count)
print("space_count",space_count)       
         