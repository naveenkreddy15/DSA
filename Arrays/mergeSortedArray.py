# Program to merge the 2 sorted arrays
def mergeSorted(arr1,arr2):
    i=0; j=0; k=0
    res = []

    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            res.append(arr1[i])
            i=i+1
        else:
            res.append(arr2[j])
            j=j+1

    #copy leftover array elements from arr1
    while(i<len(arr1)):
        res.append((arr1[i]))
        i=i+1

    #copy leftover array elements from arr2
    while(j<len(arr2)):
        res.append(arr2[j])
        j=j+1

    return res

if __name__=="__main__":
    arr1 = [1,3,5,7,9,10,11]
    arr2 = [2,4,6,19]
    result =  mergeSorted(arr1,arr2)
    print(result)