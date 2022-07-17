#Program to find the kth largest/smalllest element in an array

def largest(arr,k):
    print("sorted array is ",sorted(arr))
    return (sorted(arr)[-k:],sorted(arr)[:k])


if __name__ == "__main__":
    print(largest([-1,2,-4,-7,2-3,0,5,3],3))


