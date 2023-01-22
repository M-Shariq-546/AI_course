'''
FootBall Ground Pattern With size 10
'''


import numpy as np


def checkerboard(s):
    
    
    print("Footbal Ground pattern is : ")
    x = np.zeros((s , s) , dtype=int)
    
    x[0:s , 1] = 1
    x[0:s , 3] = 1
    x[0:s , 5] = 1
    x[0:s , 7] = 1
    x[0:s , 9] = 1
    
    print(x)


print("The Size of FootBall Ground is 10")
s = 10
checkerboard(s)
