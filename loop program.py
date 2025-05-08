# print  hello to all upto 1 to 10
# a=1
# while a<=10:
#      print("Hello to all..",a)
#      a+=1  #a=a+1 to increment value by 1
     
# print 100 to 50 decrement by 5 always

# x=100
# while x>=50:
#      print(x)
#      x-=5       
     
# x=100
# while x>=50:
#      if x%2==0:
#          print(x)
#      x-=5    
     
# x=100
# while x>=50:
#     if x%2==0:
#        print("even",x)
#     else:
#         print("odd",x)
#     x-=5    

# Q) WAP TO PRINT EVEN NUMBER FROM 121 TO 229 USING WHILE LO
# p=121
# while p<=229:
#       if(p%2==0):
#           print( p)
#       p+=1    

#Q) WAP TO PRINT ODD NUMBERS FROM 521 TO 229 USING WHILE LOOP

# p=521
# while p>=229:
#       if(p%2==1):
#           print(p)
#       p-=1    
      
# Q) WAP TO FIND SUM OF ALL EVEN NUMBERS BETWEEN 1 TO N  
 
# i=2
# sum=0
# n=int(input("Enter number:"))
# while i<=n:
#     if(i%2==0):
#       print(i)
#       sum=sum+i
#     i=i+2
# print("sum of even number",sum)

# Q) wap to find sum of all odd numbers between 1 to n

# a=1
# sum=0
# n=int(input("enter number"))
# while a<=n:
#      if a%2==1:
#          sum=sum+a
#      a=a+2
# print("sum of odd number is",sum)         

# wap to count number of digits in any number

n=int(input("enter any number"))
count=0
while n!=0:
      r=n%10    #separate digit
      count=count+1
      n//=10
print("count number of digit is",count )      
      
# dry run

# count=0
# n!=0   r=n%10    count+=1  n=n//10

# 1234!=0  r=4 count=1   1234//10--->123.4==123
# 123!=0   r=3 count=2

      
     
