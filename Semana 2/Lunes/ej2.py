num1 = input("Please enter number 1: ")
num2 = input("Please enter number 2: ")

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    if num2 == 0:
        print("Num 2 can't be 0")
    else:
        print(f"The result is:{num1/num2}")

else:
    print("Please enter a valid numbers.")
