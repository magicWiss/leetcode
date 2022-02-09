'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
'''
from collections import Counter
class Solution:
   def longestPalindrome(self, s):
        ans=0
        for v in Counter(s).values():
           ans+=v//2*2
           if v%2==1 and ans%2==0:
               ans+=1
        return ans