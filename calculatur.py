from add import add
from multi import multi
from Divide import devide
from sub import sub


def main():
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    func = input("what do you want to do? ")

    if func == "add":
        print(add(a,b))

    if func == "multi":
        print(multi(a,b))

    if func == "devide":
        print(divide(a,b))

    if func == "sub":
        print(sub(a,b))

    else:
        print("erorr")

main()