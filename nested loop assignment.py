# # i=1
# # while i<=10:
# #     print(i,end=" ")
# #     i+=1
# # # o/p==1 2 3 4 5 6 7 8 9 10

#----------------------------------------


# * * * * *
# * * * * *
# * * * * *
# * * * * *

# row=1
# while row<=4:
#        col=1
#        while col<=5:
#           print(" * ",  end=" ") # for row
#           col+=1
#        print()   # nextline
#        row+=1


#-----------------------------------------------


# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5

# # row=1
# # while row<=5:
# #       col=1
# #       while col<=row:
# #          print(col ,end=" ")
# #          col+=1
# #       print()
# #       row+=1
#-------------------------------------------------- 
     
# # 1 2 3 4 5
# # 1 2 3 4
# # 1 2 3
# # 1 2
# # 1 

# # row=5
# # while row>=1:
# #     col=1
# #     while col<=row:
# #         print(col,end=" ")
# #         col+=1
# #     print()
# #     row-=1     
#---------------------------------------------------    


# # # 5 4 3 2 1
# # # 5 4 3 2
# # # 5 4 3
# # # 5 4
# # # 5

# row=5
# while row>=1:
#      col=5
#      while col>=6-row:
#        print(col,end=" ")
#        col-=1
#      print()
#      row-=1
      
 #------------------------------------------------------------------     
#      
# # 1 
# # 1 2 1
# # 1 2 3 2 1
# # 1 2 3 4 3 2 1
# row=1
# while row>=1:
#     col=1
#     while col<=row+1:
#        print(col,end=" ")
#        col+=1
#     print()
#     row+=1
    

#-----------------------------------------------------------------


# # 1
# # 2  3   4
# # 5  6   7   8   9
# # 10 11  12  13 14  15 16
# # 17 18  19  20 21  22 23 24 25

# row=1
# rows=5
# current=1
# while row<= rows:
#    for i in range(row*2-1):
#         print(current,end=" ")
#         current+=1
#    print()
#    row+=1    
#------------------------------------------------------------------------------

# row=1
# while row<=5:                            #12345
#        col=1                             #12345  
#        while col<=5:                     #12345 
#             print(col,end="")            #12345
#             col+=1                       #12345
#        print()
#        row+=1


#-----------------------------------------
    
    
# 1
# 2 3 4
# 5 6 7 8 9
# 10 11 12 13 14 15 16

# rows = 4
# current = 1
# row = 1

# while row <= rows:
#     for i in range(row * 2 - 1):
#         print(current, end=" ")
#         current += 1
#     print()
#     row += 1

# Solve below program & write their dry run

# 1
# 2 3
# 4 5 6
# 7 8 9 10


# rows=4
# current=1
# row=1

# # while row<=rows:
#     for i in range(row):
#         print(current,end=" ")
#         current+=1
        
#     print()
#     row+=1    
#--------------------------------------------- 
#           1
#         1 2
#       1 2 3 
#     1 2 3 4
#   1 2 3 4 5 




row=1
while row<=5:
    col=row
    while col<=1:
         print(col,end=" ")
         col+=1
    print()
    row+=1    


#-----------------------------------------------------------------------
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# 6 5 4 3 2 1
# 7 6 5 4 3 2 1 




# row=1
# while row<=7:
#     col=row
#     while col>=1:
#         print(col,end=" ")
#         col-=1
#     print()
#     row+=1    


    