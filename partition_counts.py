# Austin Richards 12/19/20 22:45
'''
This code will perform the partition count function with sequence patterns defined by Euler
'''

import numpy as np 

def sub_pattern(n):
    vec = np.zeros(n+1)
    i   = 0
    j   = 1
    while i <= n:
        vec[i] = j  # fill the vector with ascending pattern 1, 2, 3, ... every other
        i += 2
        j += 1
    i = 1
    while i < n: 
        vec[i] = vec[i-1] + vec[i+1]  # fill the 0s with the sum of adjacent values
        i += 2
    
    return vec[0:n]

def operate_position(vec_a):
    n = len(vec_a)
    vec_b = np.zeros(n)
    vec_b[0] = 1
    i = 1
    while i < n:
        vec_b[i] = vec_b[i-1] + vec_a[i-1]
        i += 1
    return vec_b

def sign_pattern(vec):
    sign_vec = np.zeros_like(vec)
    n = len(vec)
    i = 1
    while i < n:
        if vec[i] <= n:
            sign_vec[int(vec[i-1])-1] = 1
            sign_vec[int(vec[i])-1]   = 1
        i += 1
    return sign_vec

def alternate_sign(vec):
    i = 0
    n = len(vec)
    j = 1
    while i < n:
        if vec[i] != 0:
            if j <= 2:
                vec[i] *=  1
                j += 1
            elif j > 2 and j <= 4:
                vec[i] *= -1
                j += 1
            else:
                j = 1
                i = i - 1
                continue
        i += 1
    return vec

def partition_count(n):
    if n == 0:
        return 1

    # initialize vectors
    a = sub_pattern(n+2)
    b = operate_position(a)
    c = sign_pattern(b)
    sign_vec = alternate_sign(c)

    # create a vector to store the solution, initialize with formality p(0) = 1
    soln = np.zeros(n)
    soln[0] = 1

    # do the partition algorithm
    for i in range(1,n):
        current_sign = sign_vec[0:i]
        current_soln = soln[0:i]
        soln[i] = sum( current_sign * current_soln )
        print(current_sign)

    return soln
        

test = partition_count(7)
print(test)