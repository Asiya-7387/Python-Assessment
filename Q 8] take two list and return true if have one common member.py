# Q 8] . Write a Python function that takes two lists and returns True if they have at least one
# common member.


l1=[1,2,3,4,5]
l2=[5,6,7,8,9]

result=False

for x in l1:
    for y in l2:
        if x==y:
            result=True
            print(result)
if result:
    print("lists have at least one common member")
else:
   print("lists do not have common member")            
  # o/p
  #
 #  True
  # lists have at least one common member#\