class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        path=[]
        def backtrack(start_num):
            if len(path)==k:
                res.append(path[:])
                return

            for num in range(start_num,n+1):
                path.append(num)
                backtrack(num+1)
                path.pop()


        backtrack(1)
        return res