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
        #7月4凑数，7月5凑数，7月6好复习通信技术和机器学习，7月7现代控制理论，7月8号争取争取学费，7月9号复习英语，7月10鸣潮更新过剧情，7月11做安全攻高防两个小时给我坐化了，没做出来
        #7月12复习英语，7月13凌晨还在背英语，7月14到家，出去玩吃饭，回来休息
