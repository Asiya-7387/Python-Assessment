#wap to create a list such that new list contains alternative even and aodd from

a=[2,4,9,7,1,55,44,87,24,12]

even=0
odd=1

c=[None]*len(a)

for l1 in a:
    if l1%2==0:
        if l1%2==0:
          if even<len(a):
            c[even]=l1
            even+=2
            
        else:
            
           if odd<len(a): 
            c[odd]=l1
            odd+=2
print(c)            
            