
# no=int(input("enter number"))
# temp=no
# sum=0
# while no>0:
#       r=no%10   # reminder
#       sum=sum + r*r*r
#       no//=10
# if temp==sum:
#    print(temp,"is armstrong number")
# else:
#   print(temp,"is not armstrong number")      
      

#WAP TO PRINT TABLE OF GIVEN NUMBER

# num=int(input("enter table of given number"))
# i=1
# while i<=10:
#       print(num,"*",i,"=",num*i)
#       i+=1 
      
# WAP TO PRINT SQUARES FROM 1TO 20


# a=1
# while a<=20:
#       sqr=a*a
#       print(sqr)
#       a+=1 

# WAP TO CHECK GIVEN NO IS PALINDROME OR NOT
#   ORIGINAL=REVERSE
 #  121=121
 
n=121
rev=0
i=n
while i>0:
     digit=i%10
     rev=(rev*10)+digit
     i//=10
if n==rev:
  print("number is palindrome") 
else:
    print("number is not palindrome")
     
 