'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''




class Solution:
    def isPalindrome(self, s: str) -> bool:
        #si analizzano tutte i caratteri a partire da 0 e si itera simultaneamente a dx e sinistra

        #casi base
        if len(s)==1 or len(s)==0:
            return True

        i=0
        j=len(s)-1

        while i<=j:
            
            #caso 1
            if s[i].lower()==s[j].lower():
                i+=1
                j-=1
            
            elif s[i].isalnum()==False:
                i+=1
            
            elif s[j].isalnum()==False:
                j-=1
            
            elif s[i].lower()!=s[j].lower():
                return False
        return True

