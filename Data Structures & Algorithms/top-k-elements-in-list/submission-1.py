class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        result = [[] for _ in range(len(nums) + 1)]
        print(result)
        print(map)
        for key,val in map.items():
            result[val].append(key)
        res = []
        for i in range(len(result)-1,0,-1):
            for j in range(len(result[i])):
                res.append(result[i][j])
                if len(res)==k:
                    return res
  
        print(res)
        return res
        