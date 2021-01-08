# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        i,j=0,n-1
        while i<j:            
            mid = (i+j)//2         
            if mountain_arr.get(mid)< mountain_arr.get(mid+1):
                i=mid+1
            else:
                j=mid
        ind = self.binary_search(mountain_arr,target,0,i)
        if ind==-1:
            ind = self.binary_search(mountain_arr,target,i+1,n-1,lambda x:-x)
        return ind
    def binary_search(self,arr,target,left,right,key=lambda x:x):
        target = key(target)
        while left<=right:
            mid = (left+right)//2
            cur = key(arr.get(mid))
            if cur==target:
                return mid
            if cur<target:
                left = mid+1               
            else:
                right=mid-1
        return -1        
