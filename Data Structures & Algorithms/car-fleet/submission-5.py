class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [[position[i], speed[i]] for i in range(len(position))]
        ps.sort(key=lambda x: x[0], reverse=True)

        time_left = [((target - ps[i][0])/ ps[i][1]) for i in range(len(ps))]
        
        stack = [time_left[0]]
        for i in range(1, len(time_left)):
            if time_left[i] > stack[-1]:
                stack.append(time_left[i])
        
        return len(stack)
        # Old
        # Time: O(n + nlogn + n^2) = O(n^2)
        # Space: O(n)

        # New
        # Time: O(n + nlogn + n)
        # Space: O(n + n)


        """
        while ps:
            ps[-1][0] = min(ps[-1][0] + ps[-1][1], target)
            for i in range(len(ps)-2,-1,-1):
                ps[i][0] = min(ps[i][0] + ps[i][1], ps[i+1][0])
            if ps[-1][0] == target:
                count += 1
                while ps and ps[-1][0] == target:
                    ps.pop()
        return count
        """