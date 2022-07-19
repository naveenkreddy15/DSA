#Program to find the pax pivot element in an rotated sorted array
def getMaxPivotAlt(arr):
    start = 0
    end = len(arr)
    mid = int(start + (end-start)/2)

    if(arr[start] < arr[end-1]):
        return end - 1

    while(start <  end):
        if(arr[mid] > arr[mid+1]):
            return mid
    # Condition checks if the start element is less than mid element, then left side of the array is sorted, we need to
    # look in the right side of the array
        if(arr[mid] > arr[start]):
            start = mid
        else:
            end = mid - 1

        mid = int(start + (end-start)/2)

    return start

if __name__ == "__main__":
    print("Program to find the max pivot element in an rotated sorted array")
    res = getMaxPivotAlt([6,7,8,9,10,1,2,3,4])
    print("result ",res)