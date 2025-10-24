def twoSum(arr, target):
    i = 0
    j = len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s > target:
            j -= 1
        elif s < target:
            i += 1
        else:
            return [i + 1, j + 1]  # 1-indexed result

print(twoSum([2, 7, 11, 15], 9))
