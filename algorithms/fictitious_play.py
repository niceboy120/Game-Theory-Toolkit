import numpy as np

# Returns Best response for row player given opponent strategy b 
def BR1(M, b):
    return np.argmax(M@b)

# Returns Best response for col player given opponent strategy a
def BR2(M, a):
    return np.argmin(M.T@a)

# Returns strategies for each iteration of Fictitious Play 
def runalg(M, x, y, T):
    n = len(M)
    for t in range(1, T):
        it1 = np.array([0]*n)
        it1[BR1(M, y[t-1])] = 1
        x.append(t/(t+1)*x[t-1] + 1/(t+1)*it1)
        jt = np.array([0]*n)
        jt[BR2(M, x[t])] = 1
        y.append(t/(t+1)*y[t-1] + 1/(t+1)*jt)
    return x, y