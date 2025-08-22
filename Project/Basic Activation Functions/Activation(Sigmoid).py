import numpy as np
import random
user_input=input("Do you wanna try this is(yes/no): ")
if user_input.lower()=='yes':
    count=1
    while True:
        if count>1:
            userinput=input("wanna continue or exit")
            if userinput.lower=='exit':
                break
            else:
                count+=1
                print("input node are there: ", ends=(""))
                n=input()
                w=np.zeros((n,3))
                for i in range(n):
                    w[i][0]=random.randint(-1,1)
                    w[i][1]=random.randint(-1,1)
                    w[i][2]=random.randint(-1,1)
                x=np.zeros((1,n))
                for i in range(1):
                    x[i][0]=int(input("Enter the X value:"))                               
                    x[i][1]=int(input("Enter the X value:"))                               
                    x[i][2]=int(input("Enter the X value:"))   
                y=np.zeros((n,1))
                for i in range(n):
                    for j in range(n):
                        y[i][0]+=x[0][j]*w[j][i]