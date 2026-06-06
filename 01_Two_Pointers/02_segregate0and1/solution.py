'''
GeeksforGeeks: https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1
Segregate 0s and 1s

Given an array arr consisting of only 0's and 1's in random order. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.
'''

class Solution:
    def segregate0and1(self, arr):
        k = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[k], arr[i] = arr[i], arr[k]
                k += 1
        return arr
    
L = list(map(int, input("Enter array of 0's and 1's: ").split()))

obj = Solution()
print("Segregated array: ", obj.segregate0and1(L))