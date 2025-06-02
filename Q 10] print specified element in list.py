# Q 10]. Write a Python program to print the numbers of a specified list after removing even
#numbers from it.

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for val in a:
#     if val % 2 == 1:
#         print(val, end=" ")


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = [val for val in a if val % 2 == 1]
print(res)