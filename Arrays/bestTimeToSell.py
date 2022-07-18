# Program to find the best time to sell stocks
def bestTimeToSell(arr):
    left = 0
    right = 1
    maxProfit = 0

    while(right < len(arr)):
        currentProfit = arr[right]-arr[left]
        if(arr[left] < arr[right]):
            maxProfit = max(currentProfit,maxProfit)
        else:
            left = right
        right +=1
    return maxProfit

if __name__ =="__main__":
    print("Program to find the best time to buy and sell stocks")
    arr=[7,1,5,3,6,4]
    res = bestTimeToSell(arr)
    print("max profit",res)

