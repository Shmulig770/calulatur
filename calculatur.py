from add import add
from multi import multi
from Divide import divide
from sub import sub
from power import power

def main():
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    func = input("what do you want to do? ")

    if func == "add":
        print(add(a,b))

    elif func == "multi":
        print(multi(a,b))

    elif func == "divide":
        print(divide(a,b))

    elif func == "sub":
        print(sub(a,b))

    elif func == "power":
        print(power(a,b))

    else:
        print("error")

main()