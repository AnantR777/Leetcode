class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, round(sqrt(n)+1)):
            if n % i == 0:
                factors.append(i)
                if i != n // i:  # Avoid adding duplicate factor for perfect squares
                    factors.append(n // i)
        factors.sort()
        if len(factors) >= k:
            return factors[k-1]
        else:
            return -1
