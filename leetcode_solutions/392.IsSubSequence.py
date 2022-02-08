'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0 and len(t)>0:
            return True
        if len(s)>len(t):
            return False
        r=set(s)

        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                
                j+=1
        if i<len(s) and j==len(t):
            return False
        return True

        