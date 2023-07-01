class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0  # Variable to count the number of elements not equal to val
    
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]  # Move the element to the front of the array
                count += 1
    
        return count
