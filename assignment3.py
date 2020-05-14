import numpy as np
from matplotlib import pyplot as plt

def create_plots():
    x = np.linspace(-2*np.pi,2*np.pi,500)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y)
    plt.plot(x, z)
    plt.show()
    return None

#create_plots()

def create_scatter_plot():
    x = np.random.normal(scale=1.5, size=500)
    y = np.random.normal(scale=1, size=500)

    plt.plot(x,y, 'x', markersize=5, alpha=1)
    plt.show()
    return None

#create_scatter_plot()

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

# print(fact(6))


def f(x):
    return x**2+x-5

# a = 0
# b = 2
# n = 50
# for i in range(n):
#     d = (a + b)/2
#     if f(d) < 0:
#         a = d
#     else:
#         b = d
#     print(d)

def g(x):
    return (x**4)-(2*x**3)-(17*x**2)+(4*x)+30
def g_prime(x):
    return (4*x**3)-(6*x**2)-(34*x)+4
# print(g(7))
# print(g_prime(-2))

def newtons_method(starting_guess, n):
    x_j = starting_guess
    for i in range(n):
        x_j = x_j - (g(x_j)/g_prime(x_j))
    return x_j

# print(newtons_method(10,5))

def integration(m):
    E = 1-np.exp(-1)
    for i in range(1,m+1):
        E = 1-(i*E)
    return E

print(integration(18))