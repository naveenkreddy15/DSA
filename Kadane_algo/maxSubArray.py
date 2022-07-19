# Program to find the max sum subarray
def maxSumArray(arr):
    currsum = 0
    maxsum = 0
    for x in arr:
        currsum = max(x,currsum + x)
        maxsum = max(maxsum,currsum)
    return maxsum

if __name__ == "__main__":
    arr=[7,1,3,-1,2,-3,0]
    print("Program to find the max subarray ",maxSumArray(arr))