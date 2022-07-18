# Program to find the max pivot element in an rotated sorted array
def getMaxPivot(arr):
    start = 0
    end = len(arr)-1

    mid = int(start + (end-start)/2)

# condition to check if array is of size one
    if(end == 0):
        return end

# condition to check if array is rotated by 0 times
    if(arr[start] < arr[end]):
        return end

    while(start<= end):
        if(arr[mid]>arr[mid+1]):
            return mid
        elif(arr[start] <= arr[mid]):
            start = mid + 1
        else:
            end = mid - 1

        mid = int(start + (end - start) / 2)

    return start

if __name__ =="__main__":
    print("Program to find the max element in the rotated sorted array !!")
    arr = [5,6,7,1,2,3]
    res = getMaxPivot(arr)
    print("max pivot element in an array ", arr," is at index ",res)

    arr = [5,6,7,1]
    res = getMaxPivot(arr)
    print("max pivot element in an array ", arr, " is at index ", res)

    arr = [1,2,3,4,5,6,7]
    res = getMaxPivot(arr)
    print("max pivot element in an array ", arr, " is at index ", res)

    arr = [5,6]
    res = getMaxPivot(arr)
    print("max pivot element in an array ", arr, " is at index ", res)

    arr = [5]
    res = getMaxPivot(arr)
    print("max pivot element in an array ", arr, " is at index ", res)
