# accept the number from user & CHECK NUMBER IS +VE,-VE,OR ZERO
num= int(input("enter number"))
if num>0:
    print("+ve number")
elif num<0:
    print("-ve number")   
else:
    print("zero") 
    
    
#  if...elif

percentage=int(input('Enter percentage'))

if percentage>80:
    print("Grade A+")
elif percentage>60 and percentage <=80  :
      print("Grade A")
elif percentage>=40 and percentage<=60:
     print("grade B")
else:
     print("you are fail")
            
    
# user select the option   to make coffee/tea  

sugar="true"
milk="true"
expresso="true"
tea_powder="false"

print("to make coffee/Tea")

if sugar:
    print("Add sugar")
if milk:
    print("add milk")
if expresso:
   print("add expresso")
if tea_powder:
    print("add tea powder")
    
