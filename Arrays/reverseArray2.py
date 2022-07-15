# Program to reverse an array after a index m
def reverseArray(arr,m):
    start = m
    end = len(arr)-1

    while(start <= end):
        arr[start],arr[end]=arr[end],arr[start]
        start = start + 1
        end = end - 1

    return arr

if __name__ == "__main__":
    inputarr = [1,2,3,4,5,6,7,8]
    print("Input array is " + str(inputarr))
    m = 2
    res = reverseArray(inputarr,m)
    print("revesed array after an index "+ str(m) + " is "+ str(res))