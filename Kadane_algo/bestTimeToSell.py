def maxProfit(A):
    best = 0
    lo = A[0]
    for x in A[1:]:
        best = max(best, x - lo)
        lo = min(lo, x)
    return best

if __name__ =="__main__":
    print("Program to find the best time to buy and sell stocks")
    arr=[7,1,3,-1,2,-3,0]
    res = maxProfit(arr)
    print("max profit",res)


