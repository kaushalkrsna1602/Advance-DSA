def peakIndexInMountainArray(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = l + ((r - l)//2)
        if arr[m + 1] > arr[m]:
            l = m +1
        else:
            r = m 
    return l 

print(peakIndexInMountainArray([0,1,0]))