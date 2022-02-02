'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

#method 1->sorting both strings and seeing if they have the same letters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len (s)!=len(t):
            return False
        
        #ordering
        s=sorted(s)
        t=sorted(t)

        return s==t