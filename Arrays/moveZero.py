# Program to move zeroes to the end of the array
def moveZero(arr):
    nonZeroIdx=0
    idx = 0

# check if next element in the array is nonzero, then swap the element with previous index element
    while(idx < len(arr)):
        if(arr[idx] != 0):
            arr[nonZeroIdx],arr[idx]=arr[idx],arr[nonZeroIdx]
            nonZeroIdx = nonZeroIdx + 1
        idx = idx + 1

    return arr

if __name__ == "__main__":
    arr = [0,1,0,4,1,0,2,4]
    result = moveZero(arr)
    print(result)