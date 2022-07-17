# Program to find the pair of elements from two arrays whose sum is closest to given number
import sys
def closestPair(nums1, nums2, total):
    i = 0
    size = len(nums1)
    j = len(nums2) - 1
    diff = sys.maxsize

# Logic is to iterate the first array from the beginning and second array from last element
# check if total of these indexes is greater than given number decrement value of index from second element and
# else if value is less given number than increment the index form first element from first array

    while (i < size and j >= 0):
        if abs(nums1[i] + nums2[j] - total) < diff:
            firstidx = i
            secondidx = j
            diff = abs(nums1[i] + nums2[j] - total)

        if (nums1[i] + nums2[j]) < total:
            i = i + 1
        else:
            j = j - 1

    return (nums1[firstidx],nums2[secondidx])

if __name__ == "__main__":
    print("Program to find the pair of elements from two arrays whose sum is closest to given number")
    nums1 = [1, 3, 5, 7, 9, 11, 15]
    nums2 = [2, 3, 7, 9, 14]
    total = 23
    print("closest pair from 2 sorted arrays are ", closestPair(nums1, nums2, total))
