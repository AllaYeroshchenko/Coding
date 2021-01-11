# 509. Fibonacci Number


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
           return 0
        x1, x2 = 0, 1
        while n>1:
            x1, x2 = x2, x1+x2
            n-=1
        return x2    



#class Solution:
#    def fib(self, n: int) -> int:
#        if n == 0:
#           return 0
#        if n == 1:
#            return 1
#        return self.fib(n-2) + self.fib(n-1)        