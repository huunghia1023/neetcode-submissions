class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countHash = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            countHash[n] = countHash.get(n, 0) + 1
        
        for i, v in countHash.items():
            freq[v].append(i)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
