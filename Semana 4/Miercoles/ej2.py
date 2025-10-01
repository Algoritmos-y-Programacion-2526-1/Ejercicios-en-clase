# FORMA 1
def calculate_peaks(mountain):
    final_peaks = []
    for index in range(len(mountain)):
        if index == 0 or index == len(mountain)-1:
            continue
        if mountain[index] > mountain[index + 1] and mountain[index] > mountain[index-1]:
            final_peaks.append(index)
    return final_peaks

print(calculate_peaks([1,4,3,8,5]))


# FORMA 1
def calculate_peaks2(mountain):
    final_peaks = []
    for index, valor in enumerate(mountain):
        if index == 0 or index == len(mountain)-1:
            continue
        if valor > mountain[index + 1] and valor > mountain[index-1]:
            final_peaks.append(index)
    return final_peaks

print(calculate_peaks2([1,4,3,8,5]))