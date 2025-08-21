import numpy as np
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
                print(f"so you will have {n*3} weights")
                print("enter the weights")
                w=np.zeros((n,3))
                for i in range(n):
                    w[i][0]=int(input("Enter the weight: "))
                    w[i][1]=int(input("Enter the weight: "))
                    w[i][2]=int(input("Enter the weight: "))
                x=np.zeros((1,n))
                for i in range(1):
                    x[i][0]=int(input("Enter the X value:"))                               
                    x[i][1]=int(input("Enter the X value:"))                               
                    x[i][2]=int(input("Enter the X value:"))   
                y=np.zeros((n,1))
                for i in range(n):
                    for j in range(n):
                        y[i][0]+=x[0][j]*w[j][i]