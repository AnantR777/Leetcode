class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n)) # max digit decides how many 1s will be present
