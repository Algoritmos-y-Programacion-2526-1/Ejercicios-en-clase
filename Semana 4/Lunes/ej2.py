def generate_pair_list(nums, n):
    final_list = []
    for i in range(n):
        final_list.append(nums[i])
        final_list.append(nums[i+n])
    return final_list

print(generate_pair_list([2,5,1,3,4,7], 3)) 