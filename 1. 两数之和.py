#哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache={}
        for i,item in enumerate(nums):
            other=target-item
            if other in cache:
                return[i,cache[other]]
            cache[item]=i
#暴力
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,item in enumerate(nums):
            for j in range(i+1,len(nums)):
                post=nums[j]
                if item+post==target:
                    return [i,j]