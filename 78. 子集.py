class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]


        def backtrack(start_index):
            res.append(path.copy())

            if start_index>=len(nums):
                return

            for i in range(start_index,len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()

        backtrack(0)
        return res
        #7月4凑数，7月5凑数
