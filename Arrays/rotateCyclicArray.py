# Program to rotate the array in cyclic form by n indexes
def rotateArray(arr,k):
    i = 0
    size = len(arr)
    temp = [0] * size

    while(i < size):
        temp[(i+k)%size] = arr[i]
        i = i + 1
    return temp

if __name__ == "__main__":
    arr=[1,2,3,4,5,1,4]
    print(rotateArray(arr,3))
