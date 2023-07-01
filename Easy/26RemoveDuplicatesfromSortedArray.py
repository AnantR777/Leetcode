class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = []
        for num in nums:
            if num not in unique_nums:
                unique_nums.append(num)
        nums[:] = unique_nums  # Update the original list
        return len(nums)
