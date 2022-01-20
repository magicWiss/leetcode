'''
ou are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''




class Solution:

    def climbStairs(self,n):
        dic = {1:1, 2:2}
        return self.ric(n,dic)
    
    def ric(self, n, dic):
        if n not in dic:
            dic[n] = self.ric(n-1,dic) + self.ric(n-2,dic)
        return dic[n]

