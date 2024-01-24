import numpy as np
from scipy.optimize import linprog

# Row Player (maximizing)
# variables z, x_1, ..., x_n
def row_strategy(M):
    m = M.shape[0]
    n = M.shape[1]

    # objective is to maximize z
    c = np.zeros(m + 1)
    c[0] = -1

    # bounds
    A_ub = []
    for i in range(n):
        A_ub.append(np.insert(-1*M[:, i], 0, 1.).tolist()[0])
    A_ub = np.array(A_ub)
    b_ub = np.zeros(n)

    # eq 
    A_eq = np.array([np.ones(m + 1)])
    A_eq[0][0] = 0
    b_eq = np.array([1])

    # bounds
    bounds = [(0, None) for i in range(m+1)]
    bounds[0] = (None, None)

    result = linprog(c, A_ub = A_ub, b_ub = b_ub, A_eq = A_eq, b_eq = b_eq, bounds = bounds)
    return result

# Col Player (maximizing)
# variables z, y_1, ..., y_n
def col_strategy(M):
    m = M.shape[0]
    n = M.shape[1]

    # objective is to minimize z
    c = np.zeros(n + 1)
    c[0] = 1

    # bounds
    A_ub = []
    for i in range(m):
        A_ub.append(np.insert(M[i], 0, -1.).tolist()[0])
    A_ub = np.array(A_ub)
    b_ub = np.zeros(m)

    # eq 
    A_eq = np.array([np.ones(n + 1)])
    A_eq[0][0] = 0
    b_eq = np.array([1])

    # bounds
    bounds = [(0, None) for i in range(m+1)]
    bounds[0] = (None, None)

    result = linprog(c, A_ub = A_ub, b_ub = b_ub, A_eq = A_eq, b_eq = b_eq, bounds = bounds)
    return result