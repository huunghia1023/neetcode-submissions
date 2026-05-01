class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkDic = {}
        for i, num in enumerate(nums):
            if num in checkDic.values():
                return True
            else:
                checkDic[i] = num
                print(checkDic)
        return False