# Program to find the peak element in an rotated sorted array

def peakElement(arr):
    start = 0
    end = len(arr)-1
    mid = int(start + (end - start) / 2)

    while(start < end):
        if(arr[mid] < arr[mid+1] and arr[mid] > arr[mid-1]):
            start = mid + 1
        else:
            end = mid
        mid = int(start + (end - start) / 2)
    return arr[start]

if __name__ == "__main__":
    print("peak element in an array is ",peakElement([5,6,7,8,9,1,2,3]))