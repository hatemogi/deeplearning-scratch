import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def result(f):
    print(f)
    for t in [f(0,0), f(1,0), f(0, 1), f(1,1)]:
      print(t)


result(AND)

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  
    b = +0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

result(NAND)

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

result(OR)