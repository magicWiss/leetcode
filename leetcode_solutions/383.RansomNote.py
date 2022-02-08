'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


'''
from typing import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magDic=Counter(magazine)

        for i in ransomNote:
            if i in magDic:
                if magDic[i]>0:
                    magDic[i]-=1
                else:
                    return False
            else:
                return False
        return True
            



        