import numpy as np
import math
import random
class activation_fnc:
    def __init__(self,y,n):
        self.y=y
        self.n=n
    def Active(self):
        result=np.zeros((1,self.n))
        for i in range(self.n):
            result[0][i]=1/(1+math.exp(-(self.y[0][i])))
        return result
class results:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def outcome(self):
        outcomes=0
        for i in range(1):
            for j in range(3):
                outcomes+=self.x[i][j]*self.y[i][j]
        return outcomes
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
                act_fnc=activation_fnc(y,n)
                result=act_fnc.Active()
                W_y=np.zeros((1,3))
                for i in range(3):
                    w[0][i]=random.randint(-1,1)
                Y_final=results(result,W_y)
                output=Y_final.outcome()
                output_final=1/(1+math.exp(-(output)))
                Y_actual=random.randint(0,1)
                loss_fnx=Y_actual-output_final
                if loss_fnx>=0.1:
                    pass                