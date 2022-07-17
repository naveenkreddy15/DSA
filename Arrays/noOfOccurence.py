# Program to find the number of occurence of an element
def firstOccu(arr,key):
    start = 0
    end = len(arr)-1

    mid = int(start + (end-start)/2)

    while(start <= end):
        if(arr[mid] == key):
            res = mid
            end = mid -1
        elif(arr[mid] > key):
            end = mid - 1
        else:
            start = mid + 1

        mid = int(start + (end-start)/2)

    return res

def secondOccu(arr,key):
    start = 0
    end = len(arr)-1

    mid = int(start + (end-start)/2)

    while(start <= end):
        if(arr[mid] == key):
            res = mid
            start = mid + 1
        elif(arr[mid] > key):
            end = mid - 1
        else:
            start = mid + 1

        mid = int(start + (end-start)/2)

    return res

if  __name__ =="__main__":
    print("Program to find the number of occurence of an element in an array !!")
    firstidx = firstOccu([1,2,3,4,5,6,6,6,7],6)
    lastidx = secondOccu([1, 2, 3, 4, 5, 6, 6, 6, 7], 6)
    print("Total number of occurerences in an array are ", (lastidx - firstidx)+1)
