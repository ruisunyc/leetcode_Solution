class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quicksort(left,right):
            if left>=right:return
            pivot = left
            i=j=pivot+1
            while j<=right:
                if nums[j]<nums[pivot]:
                    nums[i],nums[j] = nums[j],nums[i]
                    i+=1
                j+=1
            nums[pivot],nums[i-1] = nums[i-1],nums[pivot]
            quicksort(left,i-1)
            quicksort(i,right)
        quicksort(0,len(nums)-1)
        return nums
