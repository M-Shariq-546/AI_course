import numpy as np


def checkerboard(s):
    
    
    print("CheckerBoard pattern is : ")
    x = np.zeros((s , s) , dtype=int)
    
    x[1::2 , ::2] = 1
    x[::2 , 1::2] = 1
    
    
    print(x)


s = int(input("Enter the size of checkerboard : "))
checkerboard(s)