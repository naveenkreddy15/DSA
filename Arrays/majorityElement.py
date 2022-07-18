# Program to find the majority element in an array
from collections import Counter

def majorityElement(arr):
   n = len(arr)/2
   res = Counter(arr)
   out = -1
   for k,v in res.items():
      if (v > n):
         out = k

   return out

if __name__ =="__main__":
   print(majorityElement([1,2,2,2,2,3,3]))