class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
		    return 0
        elif n == 1:
		    return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

class Solution(object):
    def fib(self, n,  memo={0: 0, 1: 1}):
        """
        :type n: int
        :rtype: int
        """
        if n in memo:
		    return memo[n]
        else:
		    memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)
		    return memo[n]

        
