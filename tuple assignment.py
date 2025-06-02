# Q 1]  Write a Python program to create a tuple.

# my_tuple=()    #empty tuple

# print(my_tuple)
#====----------------

# t1=(10,39,89,56,78)
# print(t1)

#--------------------------------------------------------

# # Q 2] wap to create tuple with different data types

# t1= (1,"hello",3.4,True,[10,20,30])
# print(t1)

#-----------------------------------------------------

# # Q3] wap to create tuple with numbers and print one 

# tuple=(10,20,30,40,50)

# print(tuple)   # create tuple

# print(tuple[0])   # 

#=-----------------------------------------

# Q 4] write a python program to unpack a tuple in several variable
 
# t1=("abc","xyz","pqr")

# a,b,c=t1

# print(a)

# print(b)

# print(c)

#-----------------------------------------------

# Q 5] write a python program to add an item in a tuple.
   

# t1=(1,2,3,4,5,6)

# print(t1)

# # convert tuple to list
# l1=list(t1)

# print(l1)   # o/p-->[1,2,3,4,5,6]

# # add the element in list
# l1.append(8) 

# # convert list to tuple

# t2=tuple(l1)

# print(t2)    #o/p--->(1,2,3,4,5,6,7,8)

#--------------------------------------------------

# Q 6] write a python program to convert a tuple to string

# t=tuple("hello")
# print(t)
#---------------------------------------------------

# Q 7] write python program to get the 4th element and 4th element from last of a tuple.
#   0  1  2   3  4  5  6 7
# t1=(10,20,30,40,50,60,70,80)
# #   -8 -7 -6 -5 -4 -3 -2 -1 

# print(t1[3])      #o/p-40
# print(t1[-4])     #o/p-50
\
#----------------------------------------------

# Q 8] write a python program to reverse a tuple.

t1=(1,2,3,4,5,6,7,5,3,6)

# reverse tuple

print(t1[::-1])  # (6,3,5,7,6,5,4,3,2,1)


# #sorted tuple for descending aorder 
# # convert tuple to list


# l1=sorted(t1,reverse=True)

# print(l1)


# #convert list to tuple

# t2=tuple(l1)

# print(t2)   (7,6,6,5,5,4,3,3,2,1)

#----------------------------------

# Q 9] write a python program to find the repeated items of tuple

t1=(1,2,3,4, 1,2,3,4,4,4,4)

#t2=(10,20,30,40)

#t3=t2*3    #repeate the element 3 times
# print(t3)
print(t1)
count=t1.count(4)
print(count)

#---------------------------

# Q 10] write apython program to check whether an element exists within a tuple.

t1=(1,2,3,4,5)
i=7
if i in t1:
    print("element exists")
else:
    print("element not exist")  
          # o/p-element not exist
          
#-_----------------------------

# Q 11] write a python program to convert list to a tuple

# l1=[10,30,50,30,67,37,52,89] 

# t2=tuple(l1)

# print(t2)   #o/p--(10,30,50,30,67,37,52,89)
       
#--------------------------------------------    

#Q12] write a program to remove an  item  from a tuple

# convert tuple to list,remove from list,convert list to tuple

# t1=(10,60,50,20,40)     # create tuple

# print(t1)            # o/p- (10 60 50 20 40)


# l1=list(t1)              # convert tuple to list
# l1.remove(50)            # remove the item from list    
# t2=tuple(l1)              # convert list to tuple

# print(t2)                     #o/p==(10 60 20 40)

#---------------------------------------

# Q 13] write a python program to slice a tuple
#   0 1 2 3 4 5 6 7 8
t1=(1,2,3,4,5,6,7,8,9)

print(t1[2:6])  # 0/p--(3,4,5,6)

#--------------------------

# Q14] write a python program to find the index of an item of a tuple.

t1=(10,20,30,40,50)

print('index ',t1.index(40))  #o/p--index 3

print(t1[3])  #o/p=40

#------------------------------------------

# Q 15] write a python program to find the length of a tuple

s1=(23,45,67,98,56,34,67,24)

print(len(s1))

#--------------------------------------

# Q 16] write a python program to sort list of tuple based on sum.

#input:[(4,5),(2,3),(6,7),(2,8)]

#output:[(2,3),(4,5),(2,8),(6,7=]
                          
l1=[(4,5),(2,3),(6,7),(2,8)]

t1=tuple(l1)
print(t1)
     
t2=sorted(t1,key=lambda t1:sum(t1))

print(t2)








