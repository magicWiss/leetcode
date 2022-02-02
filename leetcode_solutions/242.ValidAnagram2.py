'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

#method 2->creating two Counter maps (key->char, value->occ)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        c1=Counter(s)
        c2=Counter(t)
        if len(c2)!=len(c1):
            return False
        
        for k,v in c1.items():
            if c2[k]!=v:
                return False
        return True