#Program to sort the elements o's,1's and 2's in the list
def sortColors(arr):
    cnt0 = arr.count(0)
    cnt1 = arr.count(1)
    cnt2 = arr.count(2)
    idx = 0
    print("cnt0,cnt1.cnt2",cnt0,cnt1,cnt2)

    while (cnt0  > 0):
        arr[idx] = 0
        cnt0 = cnt0 - 1
        idx = idx + 1

    while (cnt1  > 0):
        arr[idx] = 1
        cnt1 = cnt1 - 1
        idx = idx + 1

    while (cnt2  > 0):
        arr[idx] = 2
        cnt2 = cnt2 - 1
        idx = idx + 1

    return arr

if __name__ == "__main__":
    print(sortColors([0,1,2,0,1,2,0,2,1,0,1,2,1]))