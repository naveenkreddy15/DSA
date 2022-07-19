# Program to compute the number closest to squareroot of a number
def squareRoot(num):
    start = 0
    end = num + 1
    mid = int(start + (end-start)/2)

    while(start < end):
        squaredVal = mid * mid
        if(squaredVal > num):
            end = mid
        else:
            start = mid + 1
        mid = int(start + (end-start)/2)

    return start-1

if __name__ == "__main__":
    print("Program to find the min pivot element in an rotated sorted array")
    res = squareRoot(49)
    print("result ",res)