import numpy as np


def first_rpt(M):
    original_matrix = M.copy()
    for i in range(len(M)):
        if i > 0:
            original_matrix[i] = M[0]
    return original_matrix

M = [(1,2,3,4),(5,6,7,8),(9,1,2,3)]
#print(first_rpt(M))

def matrix_sum(A):
    total = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            total = total + A[i][j]
    return total

A=np.array([[1,-1,2,-3,1,1],[-2,-2,0,1,1,-5],[1,1,1,1,-2,-1]])
#print(matrix_sum(A))

long_list = [pow(.5,i+1) for i in range(100)]
#print(long_list)

very_long_list = [pow(j,i) for i in range(1,100) for j in range(1,4)]
#print(very_long_list)
print(np.exp(np.cos(3)))
my_var = (np.exp(5)-np.log(np.sqrt(5)))/(np.exp(np.cos(3)))
print(my_var)