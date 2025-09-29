def suma_divisible(n):
    total = 0
    for number in range(1,n+1):
        if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
            total += number

    return total

total = suma_divisible(7)
print(f"Result:{total}")
