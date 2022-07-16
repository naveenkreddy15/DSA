# Program to move the negative elements to the end of the array

def moveNegativeElements(arr):
    size = len(arr) -1
    idx = 0

    while(idx < size):
        if(arr[idx] < 0):
            arr[size],arr[idx] = arr[idx],arr[size]
            size = size - 1
        idx = idx + 1

    return arr

if __name__ == "__main__":
    print("Program to move the negative elements to the end of the array")
    print(moveNegativeElements([1,-2,3,1,-2,-5,1]))
