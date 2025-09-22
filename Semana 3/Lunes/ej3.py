nums = [1,2,3,1,1,3]
cont = 0
pares = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            cont += 1
            pares.append([i,j])

print(cont)
print(pares)