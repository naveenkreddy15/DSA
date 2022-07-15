# program to check if array is rotated and sorted
def checkRotateArray(arr):
    size = len(arr)
    start = 1
    counter = 0

# idea is to check if previous element is greater
# than the current element in the array. if yes, then increment the counter by 1
# after completion of the iteratoin. if counter is equal to one then its a rotated array else not
    while(start < size):
        if(arr[start-1] > arr[start]):
            counter = counter + 1
        start = start + 1

    if (arr[size-1] > arr[0]):
        counter = counter + 1
    return counter

if __name__ == "__main__":
    res = checkRotateArray([1,2,3,4])
    if(res == 1):
        print("Given array is rotated array")
    else:
        print("Given array is not rotated array")