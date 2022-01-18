'''
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        out=0
        space=False
        j=len(s)-1
        print(j)
        while j>=0:
            
            if s[j]==" " and space==True:
                return out
            
            if s[j]!=" " and space==False:
                space=True
            
            if s[j]!=" " and space==True:
                out+=1
            j-=1


        return out


        