# Program to find the pivot element in an array
def getMinPivot(arr):
    start = 0
    end = len(arr)-1
    mid = int(start + (end-start)/2)

    # condition to check if there is only one element in the array
    if(end == 0):
        return end

    # condition to check if first element in the array is peak element
    # i.e array elements are not rotated
    if(arr[start] < arr[end]):
        return start

    while start <= end:
        if arr[mid] > arr[mid+1]:
            return mid + 1
        elif arr[start] <= arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

        mid = int(start + (end-start)/2)

    return start

if __name__ == "__main__":
    print("Program to find the pivot element in an array !!")
    arr = [5,6,7,1,2,3]
    res = getMinPivot(arr)
    print("min pivot element in an array ", arr," is at index ",res)

    arr = [5,6,7,1]
    res = getMinPivot(arr)
    print("min pivot element in an array ", arr, " is at index ", res)

    arr = [1,2,3,4,5,6,7]
    res = getMinPivot(arr)
    print("min pivot element in an array ", arr, " is at index ", res)

    arr = [5,6]
    res = getMinPivot(arr)
    print("min pivot element in an array ", arr, " is at index ", res)

    arr = [5]
    res = getMinPivot(arr)
    print("min pivot element in an array ", arr, " is at index ", res)