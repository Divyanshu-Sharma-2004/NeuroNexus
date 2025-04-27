def add(num1,num2):
    res = num1+num2
    print(f"The addition of {num1} and {num2} is {res}")

def sub(num1,num2):
    res = num1-num2
    print(f"The Subtraction of {num1} and {num2} is {res}")

def mul(num1,num2):
    res = num1*num2
    print(f"The multiplication of {num1} and {num2} is {res}")

def div(num1,num2):
    res = num1/num2
    print(f"The division of {num1} from {num2} is {res}")

def mod(num1,num2):
    res = num1%num2
    print(f"The module of {num1} from {num2} is {res}")


def main():
    num1 = int(input("Enter your 1st number : "))
    num2 = int(input("Enter your 2nd number : "))

    print("\n----List of Operations----")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Module (%)")

    choice = int(input("\nEnter your choice of operation (1 - 5) : "))

    match choice:
        case 1:
            add(num1,num2)
        case 2:
            sub(num1,num2)
        case 3:
            mul(num1,num2)
        case 4:
            div(num1,num2)
        case 5:
            mod(num1,num2)
        case _:
            print("\nInvalid choice")

if __name__ == "__main__":
    main()
