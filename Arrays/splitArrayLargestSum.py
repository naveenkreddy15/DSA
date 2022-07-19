#410. Split Array Largest Sum [Hard]
def splitArray(nums,m):
    def feasible(threshold):
        total = 0
        count = 1

        for num in nums:
            total = total + num
            if total > threshold:
                total = num
                count = count + 1
                if count > m:
                    return False
        return True

    start,end = max(nums),sum(nums)
    mid = int(start + (end-start)/2)
    while(start <  end):
        if feasible(mid):
            end = mid
        else:
            start = mid + 1
        mid = int(start + (end - start) / 2)
    return start

if __name__ == "__main__":
    print("Program to split largest sum subarray")
    res = splitArray([9,8,1,2,3,4],2)
    print("largest sum sub array  ",res)