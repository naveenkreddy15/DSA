#Program to merge the 2 sorted array into first array
def mergeSortedarray(arr1,arr2,firstarrlen,secondarrlen):
    i = firstarrlen
    j = secondarrlen
    last = firstarrlen + secondarrlen -1

    while(i > 0 and j > 0):
        if(arr1[i-1] > arr2[j-1]):
            arr1[last] = arr1[i-1]
            i = i - 1
        else:
            arr1[last] = arr2[j-1]
            j = j - 1
        last = last - 1

    while j > 0:
        arr1[last] =arr2[j-1]
        last = last - 1
        j = j - 1
    return arr1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]; m = 3; nums2 = [2, 5, 6]; n = 3
    print("result of sorted array for testcase1 ",mergeSortedarray(nums1,nums2,m,n))

    nums1 = [1]; m = 1; nums2 = []; n = 0
    print("result of sorted array for testcase2 ", mergeSortedarray(nums1, nums2, m, n))

    nums1 = [0,0]; m = 0; nums2 = [2,3]; n = 2
    print("result of sorted array for testcase3 ", mergeSortedarray(nums1, nums2, m, n))