def shipWithinDays(weights,D):
    def feasible(capacity):
        days = 1
        total = 0
        for weight in weights:
            total = total + weight
            if total >  capacity:
                total = weight
                days = days + 1
                if days > D:
                    return False
        return True

    left,right = max(weights),sum(weights)
    mid = int(left + (right-left)/2)
    while(left < right):
        if(feasible(mid)):
            right = mid
        else:
            left = mid + 1
        mid = int(left + (right-left)/2)

    return left

if __name__ == "__main__":
    print("Program to find the min pivot element in an rotated sorted array")
    weights = [1,2,3,1,1]
    D = 4
    res = shipWithinDays(weights,D)
    print("result ",res)