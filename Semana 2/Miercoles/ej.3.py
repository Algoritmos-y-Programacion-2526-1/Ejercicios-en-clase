acum = 0
while True:
    number = int(input("Please enter a number: "))
    if number >= 0:
        acum += number
    else:
        break

print(f"The result is: {acum}")