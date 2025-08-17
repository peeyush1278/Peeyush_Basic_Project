def add(x,y):
    for i in range(len(x)):
        x[i] += y[i]
    return x

def mul(x,y):
    for i in range(len(x)):
        x[i] *= y[i]
    return x

answer=input("Do you want to continue the process? (yes/no): ")
answer=answer.lower()
while answer == "yes":
    Size=int(input("Enter the size of the vectors: "))
    x = [0] * Size
    y = [0] * Size
    for i in range(Size):
        x[i] = int(input(f"Enter element {i+1} of vector x: "))
    for i in range(Size):
        y[i] = int(input(f"Enter element {i+1} of vector y: "))
    Operation=input("Enter the operation (add/mul): ").lower()
    if Operation == "add":
        result = add(x, y)
        print("Result of addition:", result)
    elif Operation == "mul":
        result = mul(x, y)
        print("Result of multiplication:", result)
    else:
        print("Invalid operation. Please enter 'add' or 'mul'.")
        continue
    answer=input("Do you want to continue the process? (yes/no): ")
