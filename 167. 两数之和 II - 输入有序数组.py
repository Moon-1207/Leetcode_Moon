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
    
    #题目数组有序&找两个数，两个数需要满足某个制约条件。选择使用双指针
    #双指针，左指针向右，右指针向左。
