# Program to rotate the sorted array by given number
def rotateArray(arr,size,idx):
    i = 0
    idx = idx % size
    j = size - idx
    temp = [] * size

    while idx > 0:
        temp.append(arr[size-idx])
        idx = idx - 1

    temp.extend(arr[:j])

    return temp

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    size = len(arr)
    idx = 8
    print("Array after rotating by ",idx," is ", rotateArray(arr,size,idx))