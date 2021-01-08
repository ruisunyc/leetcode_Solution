class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k==0:return []
        target = k-1       
        def quicksort(arr,left,right):
            ind = random.randint(left,right)
            arr[left],arr[ind] = arr[ind],arr[left]
            pivot = left
            i=j=left+1
            while j<=right:
                if arr[j]<arr[pivot]:
                    arr[i],arr[j] = arr[j],arr[i]
                    i+=1
                j+=1
            arr[pivot],arr[i-1] = arr[i-1],arr[pivot]
            return i-1
        left,right = 0,len(arr)-1
        while left<=right:
            cur = quicksort(arr,left,right)
            if cur<target:left=cur+1
            elif cur>target:right= cur-1
            else:return arr[:cur+1]