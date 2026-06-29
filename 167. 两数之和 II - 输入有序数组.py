class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left!=right:
            my_sum=numbers[left]+numbers[right]
            if my_sum==target:
                return [left+1,right+1]
            elif my_sum>target:
                right-=1
            elif my_sum<target:
                left+=1