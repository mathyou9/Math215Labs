import numpy as np
def augment(A,b):
    Ab = np.column_stack((A,b))
    return Ab

# print(augment(np.array([[1,1,1],[1,4,2],[4,7,8]]), np.array([1,3,9])))

def first_column_zeroes(A):
    
    for i in range(1,A.shape[0]):
        A[i,:] = A[i,:] - A[i,0]/A[0,0]*A[0,:]
    return A

# print(first_column_zeroes(np.array([[2,1,3,1],[1,2,-1,2.5],[4,2,-1,1]])))

def row_echelon(A,b):
    Ab = np.column_stack((A,b))
    for i in range(Ab.shape[1]):
        for j in range(i+1,Ab.shape[0]):
            Ab[j,:] = Ab[j,:] - ((Ab[j,i]/Ab[i,i])*Ab[i,:])
    return Ab
# print(row_echelon(np.array([[3.,1.,-2],[1.,2.,-5.],[2.,-4.,1.]]),np.array([1.1,2,-3])))

def LU_decomposition(A):
    m,n = A.shape
    U = np.copy(A)
    L = np.identity(len(A))
    for j in range(n):
        for i in range(j+1,m):
            L[i,j] = U[i,j]/U[j,j]
            U[i,:] = U[i,:] - L[i,j]*U[j,:]
    return L,U

# print(LU_decomposition(np.array([[3,1,-2],[1.5,2,-5],[2,-4,1]])))

def forward_substitution(L,b):
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - y.dot(L[i,:]))/L[i,i]
    return y

# print(forward_substitution(np.array([[1,0,0],[3,1,0],[-1.1,2,1]]), np.array([-2.1,1,-1])))

def back_substitution(U,y):
    n = len(y)
    x = np.zeros(n)
    for i in range(1,n+1):
        x[n-i] = (y[n-i] - x.dot(U[n-i,:]))/U[n-i,n-i]
    return x

# print(back_substitution(np.array([[2,-3.1,1],[0,1,3],[0,0,4]]), np.array([1,-2.1,3])))

# print(back_substitution(np.array([[1,0,0],[3,1,0],[-1.1,2,1]]), np.array([-2.1,1,-1])))

def LU_solver(A,b):
    L,U = LU_decomposition(A)
    y = forward_substitution(L,b)
    x = back_substitution(U,y)
    return x

print(LU_solver(np.array([[3,1,-2],[1.5,2,-5],[2,-4,1]]), np.array([1.1,3,-2])))