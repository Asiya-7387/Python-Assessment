
# Q 6] Write a Python program to remove duplicates from a list.

l1=[1,2,2,3,4,7,4,4,8,9,4]

a=[]

for x in l1:
    if x not in a:
        a.append(x)
print(a)        