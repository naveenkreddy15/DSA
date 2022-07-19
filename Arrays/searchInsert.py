# Program to find the Search Insert Position in an array
def searchInsert(arr,target):
    start = 0
    end = len(arr)
    mid = int(start + (end-start)/2)

    if(arr[start] > target):
        return start
    if(target > arr[end-1]):
        return end

    while(start < end):
        if(arr[mid] == target):
            return mid
        if (target < arr[mid] and target > arr[mid-1]):
            return mid
        if(target > arr[mid] and target < arr[mid+1]):
            return mid + 1
        if(target > arr[mid]):
            start = mid + 1
        else:
            end = mid
        mid = int(start + (end-start)/2)

if __name__ == "__main__":
    print("Program to find the min pivot element in sorted array")
    arr = [1,4,6,7,9,10]
    target = 0
    print("target is can be inserted or found at index",searchInsert(arr,target))
