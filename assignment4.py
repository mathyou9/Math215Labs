import numpy as np
x_val = 1
y_val = 1

def jacobi1_iteration(x,y):
    new_x = (6+y)/7
    new_y = (x+4)/5
    return [new_x, new_y]

# print(jacobi1_iteration(3,5))

def jacobi1_method(n):
    x_n = 0
    y_n = 0
    for i in range(n):
        [x_n, y_n] = jacobi1_iteration(x_n, y_n)
    return [x_n, y_n]

# print(jacobi1_method(6))

def gs1_iteration(x,y):
    new_x = (6+y)/7
    new_y = (new_x+4)/5
    return [new_x, new_y]

# print(gs1_iteration(3,5))

def gs1_method(n):
    x_n = 0
    y_n = 0
    for i in range(n):
        [x_n, y_n] = gs1_iteration(x_n, y_n)
    return [x_n, y_n]

# print(gs1_method(3))

def gs1_error(n):
    b = gs1_method(n)
    a = [1,1]
    return np.linalg.norm(np.array(a) - np.array(b))
# print(gs1_error(3))

def gs2_iteration(x,y):
    new_x = y+1
    new_y = 5-(2*new_x)
    return [new_x, new_y]

def gs2_method(n):
    x_n = 0
    y_n = 0
    for i in range(n):
        [x_n, y_n] = gs2_iteration(x_n, y_n)
    return [x_n, y_n]

def gs2_error(n):
    b = gs2_method(n)
    a = [2,1]
    return np.linalg.norm(np.array(a) - np.array(b))

# print(gs2_method(5))
# print(gs2_error(3))

def gs3_iteration(x,y,z):
    new_x = (2*y-3*z-8)/5
    new_y = (-new_x+4*z+102)/4
    new_z = (2*new_x+2*new_y-90)/4
    return [new_x, new_y, new_z]

def gs3_method(n):
    x_n = 0
    y_n = 0
    z_n = 0
    for i in range(n):
        [x_n, y_n, z_n] = gs3_iteration(x_n, y_n, z_n)
    return [x_n, y_n, z_n]

def gs3_error(n):
    b = gs3_method(n)
    a = [10,11,-12]
    return np.linalg.norm(np.array(a) - np.array(b))

print(gs3_method(4))