# wap to remove  to find duplicate elements in list
#c   0 1   2  3  4  5  6  7  8  9  106
#d     1  2   3  4 5  6   7 8 9 10


a =[10,20,30,40,50,80,12,14,14,10,12]
b=[]

for c in range(len(a)):# store index  outer for loop
    for d in range(c+1,len(a)):  # range 1-10
        if a[c]==a[d] and a[c] not in b:  
           b.append (a[c])
    print (b)

# dry run

#reange[11]   c=0   c+1,11 a[c]==a[d]  



    