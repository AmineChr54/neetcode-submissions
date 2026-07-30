class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            map[num] = map.get(num,0)+1

        result = [[] for _ in range(len(nums) + 1)]
        for key,val in map.items():
            result[val].append(key)

        res = []
        for i in range(len(result)-1,0,-1):
            for val in result[i]:
                res.append(val)
                if len(res)==k:
                    return res
  
        return res
        