class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        a, b = min(nums), max(nums)
        while a < b:
            mid = (a + b) // 2
            total1, total2 = 0, 0
            for i in range(len(nums)):
                total1 += abs(mid - nums[i])*cost[i]
                total2 += abs(mid + 1 - nums[i])*cost[i]
            if total1 < total2:
                b = mid
            else:
                a = mid + 1
        output = 0
        for i in range(len(nums)):
            output += abs(a - nums[i])*cost[i]
        return output
