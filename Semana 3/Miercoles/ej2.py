accounts = [    
    [1, 2, 3], 
    [3, 2, 1], 
    [4, 5, 6]
]

riq_max = 0

for account in accounts:
    if sum(account) > riq_max:
        riq_max = sum(account)

print(riq_max)
