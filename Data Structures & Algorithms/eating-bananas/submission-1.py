class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            #print(l , m , r)
            ########
            total_hours = 0
            for pile in piles:
                number_of_hours = math.ceil(pile / m)
                total_hours = total_hours + number_of_hours
            #########
            if total_hours <= h:
                r = m
            else:   
                l = m + 1 

        return r
        
        
        
        
        
        """for k in range(1, max(piles)+1):
            total_hours = 0
            for pile in piles:
                number_of_hours = math.ceil(pile / k)
                total_hours = total_hours + number_of_hours
            if total_hours <= h:
                return k
        # Time complexity ist O(n*max(piles))"""
