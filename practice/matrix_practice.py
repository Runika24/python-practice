##Given a binary matrix of dimensions M * N. One can perform the given operation in the matrix.

# If the value of matrix[i][j] is 0, then traverse in the same direction and check the next value.
# If the value of matrix[i][j] is 1, then update matrix[i][j] to 0 and change the current direction
mat =[
     [0,1],
     [1,0]
]
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i>j :    
            if mat[i][j] == 0 or mat[j][i] == 0:
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            if mat[i][j]==1 or mat[j][i]:
                 mat[i][j] =0
# Print resulting matrix
for i in range(len(mat)):
    for j  in range(len(mat[i])):
            print(mat[i][j], end = " ")
    print()        

