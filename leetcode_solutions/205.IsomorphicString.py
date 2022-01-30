'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map1={}         #dict of s
        map2={}         #dict of t

        for i,j in zip(s,t):

            if i not in map1:
                map1[i]=j
            if j not in map2:
                map2[j]=i
            
            if map1[i]!=j or map2[j]!=i:
                return False

       

            
        return True