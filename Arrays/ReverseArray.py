#Program to reverse the array elements
def reverseArray(arr):
    start = 0
    end = len(arr)-1
    while start <  end:
        arr[start],arr[end] = arr[end],arr[start]
        start = start + 1
        end = end - 1
    return arr

if __name__ == "__main__":
    res = reverseArray([1,2,3,4,5])
    print(res)