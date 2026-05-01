class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
      
        if n == 1:
            return 1
        elif n == 2:
            return 2
        if n in self.memo:
            return self.memo[n]
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.memo[n] = result
        return self.memo[n]