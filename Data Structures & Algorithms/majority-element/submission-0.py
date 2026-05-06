class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashset = {}
        count_max, res = 0, 0
        for n in nums:
            hashset[n] = hashset.get(n, 0) + 1
            res = n if hashset[n] > count_max else res
            count_max = max(hashset[n], count_max)
            
        return res


            
        
        