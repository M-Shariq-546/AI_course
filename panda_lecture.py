import pandas as pd
import numpy as np
#creating dataframes with different data structures

# arr = np.array([['Moeez' ,50 , 3.7 , 'Lahore', 1],
#                 ['Ali', 45 , 3.1 , 'Lahore' , 2],
#                 ['Shariq', 55 , 3.5 , 'Lahore', 3]
#                 ])


# df =pd.DataFrame(arr , columns=['Name' , 'Value' , 'CGPA' , 'City' , 'Rank']) 

list = [['Moeez' ,25 , 3.7 , 'Lahore', 1],
                ['Ali', 22 , 3.1 , 'Lahore' , 2],
                ['Shariq', 23 , 3.5 , 'Lahore', 3]
                ]


df =pd.DataFrame(list, columns=['Name' , 'Age' , 'CGPA' , 'City' , 'Rank']) 

#df1 = df[::2]

df1 = df.drop([1] , axis=0)

df2 = df.iloc[::1]


#Apply function

def old(Age):
    if(Age>24):
        return 'Old'
    else: 
        return 'Young'

df3=df['Age'].apply(old) 



#Lambda function

old = lambda Age: "Old" if Age>24 else "Young"

df['Status'] = df['Age'].apply(old)

print(df)