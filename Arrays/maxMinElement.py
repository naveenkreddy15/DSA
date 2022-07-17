# program to find the min and max element of the array

def minMaxArray(arr):
    size = len(arr)

#condition to check if atleast 1 element exists
    if(size == 0):
        raise Exception("Please provide atleast one element")

# Condition to check if there are even elements
# then get the max and min elements using the first 2 index elements
    if (size%2 == 0):
        mx = max(arr[0],arr[1])
        mn = min(arr[0],arr[1])
        i = 2

# Condition to check if there are odd elements in the array
# assign the first element as max and min
    elif(size%2 != 0):
        mx = mn = arr[0]
        i = 1

    while(i <= size -1):
        if(arr[i] > arr[i+1]):
            mx = max(mx,arr[i])
            mn = min(mn,arr[i+1])
        else:
            mx = max(mx,arr[i+1])
            mn = min(mn,arr[i])
        i=i+2

    return(mx,mn)

if __name__ == "__main__":
    print("Program to find the max and min element in an array")
    nums1 = [1,-1,4,2,6,4,2]
    print("max and min elements are (max,min",minMaxArray(nums1))

    print("Program to find the max and min element in an array")
    nums2 = [1]
    print("max and min elements are (max,min", minMaxArray(nums2))

    print("Program to find the max and min element in an array")
    nums3 = [1,0]
    print("max and min elements are (max,min", minMaxArray(nums3))

    print("Program to find the max and min element in an array")
    nums4 = [0]
    print("max and min elements are (max,min", minMaxArray(nums4))

