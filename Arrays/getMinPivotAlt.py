# Program to find the pivot element(min) in an array
def getMinPivotAlt(arr):
    start = 0
    end = len(arr)
    mid = int(start + (end-start)/2)

    if(arr[start] < arr[end-1]):
        return start

    while(start <  end):
        if(arr[mid] > arr[mid+1]):
            return mid + 1
        if(arr[start] < arr[mid]):
            start = mid
        else:
            end = mid - 1
        mid = (start + (end-start)/2)

    return start

if __name__ == "__main__":
    print("Program to find the min pivot element in an rotated sorted array")
    res = getMinPivotAlt([9,8,1,2,3,4])
    print("result ",res)