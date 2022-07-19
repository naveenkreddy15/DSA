# https://leetcode.com/problems/koko-eating-bananas/

def minEatingSpeed(piles,h):
    def feasible(threshold):
        total = 0
        count = 1
        for pile in piles:
            total = total + pile
            if total > threshold:
                total = pile
                count = count + 1
                if count > h:
                    return False

        return True

    start,end = max(piles),sum(piles)
    mid = int(start + (end-start)/2)

    while(start < end):
        if feasible(mid):
            end = mid
        else:
            start = mid + 1
        mid = int(start + (end - start) / 2)

    return start


if __name__ == "__main__":
    print("Program to find minimum integer k such that she can eat all the bananas within h hours")
    piles = [30,11,23,4,20]
    h = 6
    res = minEatingSpeed(piles,h)
    print("result ",res)




