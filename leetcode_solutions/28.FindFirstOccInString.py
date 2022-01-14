'''
mplement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    def strStr(self, input: str, u: str) -> int:
        
        #caso bae
        if len(input)==0 and len(u)==0:
            return 0
        
        #se la sub-string è maggiore della stringa i, allora u non è contenuta
        if len(u)>len(input):
            return -1

        #caso concreto
        x=len(u)-1              #definisce l'upper bound della sub-string

        i=0                     #definisce il lower bound


        while x<len(input):
            
            
            current_sub=input[i:x+1]          #la substring

            

            if current_sub==u:
                return i
            
            i+=1
            x+=1
        return -1
