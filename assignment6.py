import numpy as np
import matplotlib.pyplot as plt

X1 = np.array([[1,5],[1,10],[1,15],[1,20],[1,25],[1,30],[1,35],[1,40],[1,45],[1,50]])
Y1 = np.array([3.33,4.43,4.39,5.23,5.67,6.06,7.01,7.16,8.03,8.78])

# print(X1)

XT = np.transpose(X1)
normal_coef1 = np.matmul(XT,X1)
normal_vect1 = np.matmul(XT,Y1)

# print(normal_coef1)
# print(normal_vect1)
# print("hello")

beta1 = np.linalg.solve(normal_coef1, normal_vect1)

# print(beta1)

def ls1_line(x):
    y = beta1[1]*x+beta1[0]
    return y

# print(ls1_line(12.5))

def create_plots1():
    n = np.linspace(0,60,10)
    m = ls1_line(n)
    a = np.linspace(0,60,10)
    b = Y1
    plt.plot(n,m)
    plt.plot(a,b,'ro')
    plt.axis([0,60,0,20])
    plt.show()
    return None

create_plots1()

print(ls1_line(60))

