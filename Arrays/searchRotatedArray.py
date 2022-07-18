# Program to search an element in an rotated sorted array
def getPivot(arr):
    start = 0
    end = len(arr)-1
    mid = int(start + (end-start)/2)

    if(end == 0):
        return start

    if(arr[start] < arr[end]):
        return end
    #[4,5,6,7,1,3]
    while(start <= end):
        if(arr[mid] > arr[mid+1]):
            return mid
        elif(arr[start] <= arr[mid]):
            start = mid + 1
        else:
            end = mid - 1
        mid = int(start + (end-start)/2)

    return start

def searchElement(arr,s,e,key):
    start = s
    end = e
    mid = int(start + (end -start)/2)

    while(start <= end):
        if(arr[mid] == key):
            return mid
        elif(arr[mid] > key):
            end = mid - 1
        else:
            start = mid + 1

        mid = int(start + (end-start)/2)
    return start

if __name__ =="__main__":
    print("program to search an element in an rotated sorted array !!")
    arr = [3,4,5,6,7,8,9,1]
    res = getPivot(arr)
    print("index element of arr",arr," is at index ",res)
    key = 1
    if (key >= arr[res] and key <= arr[len(arr)-1]):
        print("First Element ",key," is at index ",searchElement(arr,res,len(arr)-1,key))
    else:
        print("second Element ",key," is at index ",searchElement(arr,0,res-1,key))

