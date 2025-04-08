mat1 =[
    [1,2,3],
    [2,4,0],
    [7,9,7]
]

for i in mat1:
   print (i)

#for accessing every element

for i in mat1:
   for j in i:
       print(j)    
#for accessing individual element
print(mat1[1][2]) 

##
#sum =0;
for i in range(len(mat1)):
    print(mat1[i])
    for j in range(len(mat1[i])):
       print(i,j, mat1[i][j])
       #diagonals sum.............
       if i==j or i+j ==len(mat1)-1:
            print(mat1[i][j])
    #     if i+j ==len(mat1)-1:
    #         print(mat1[i][j])    
    #     if mat1[i][j] %2 ==0:
    #         print(mat1[i][j]) 
    #         #for getting only boundary elements of a matrix.   
    #     if i ==0 or j ==0 or i ==len(mat1)-1 or j ==len(mat1[i])-1:
    #         print(mat1[i][j]) 

    #         print(mat1[i][j] , end='   ')
    #     else:
    #         print(' ',end='  ')
    # print()
            sum = sum+ mat1[i][j]
print(sum)  
  
#   -------------transpose of a matrix  ->i,j =j,i-------------------------------

for i in range(len(mat1)):
    for j in range(len(mat1[i])):
        if i> j:
            mat1[i][j] , mat1[j][i] = mat1[j][i] , mat1[i][j]   
for i in range(len(mat1)):
    for j in range(len(mat1[i])):
        print(mat1[i][j] , end='   ')
    print()

#addition of two matrix
