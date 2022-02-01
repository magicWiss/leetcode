'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

More generally, for any number n > 0
n & n - 1 removes the last 1 in the binary form of n
if and only if n is a power of two, there is only one 1 in the binary form of n
'''
import math as mt
class Solution(object):
    def isPowerOfTwo(self, n):
        return n and not (n & n - 1) #mette bit a bit in and n e n-1. Se è
    
         