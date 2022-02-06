'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s=list(s)
        if len(s)==0:
            return None
        
        vowels=("a","e","i","o","u","A","E","I","O","U")

        i,j=0,len(s)-1
        while i<j:
            if s[i] not in vowels:
                i+=1
            if s[j] not in vowels:
                j-=1
            if s[j] in vowels and s[i] in vowels:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)
