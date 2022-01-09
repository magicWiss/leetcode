'''
Created on 5 gen 2022
Given a string s, return the longest palindromic substring in s.
@author: Wissel

SOLUZIONE:
per ogni carattere della stringa, si prende il corrente e si considera il centro della sub-stringa.
Si espande a destra e sinistra analizzando i caratteri nell'INTORNO, verificando che la sub-stringa creata risulti 
essere palindroma.

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        stringa_out=""                  #stringa da ritornare
        max_len=0                       #lunghezza della stirnga corrente
        
        for i in range(len(s)):         #per ogni carattere presente i s
            
            #dispari
            dx,sx=i,i                     #iteratori a dx e sx
            
            while dx<len(s) and sx>=0 and s[dx]==s[sx]:        
                
                #aggiorno la sub
                if(max_len< dx-sx+1):
                    stringa_out=s[sx:dx+1]                  #split della stringa
                    max_len=dx-sx+1                         #aggiornamento della dim massima
                
                sx-=1
                dx+=1
                    
            #pari
            
            dx,sx=i+1,i                     #iteratori a dx e sx
            
            while dx<len(s) and sx>=0 and s[dx]==s[sx]:        
                
                #aggiorno la sub
                if(max_len< dx-sx+1):
                    stringa_out=s[sx:dx+1]                  #split della stringa
                    max_len=dx-sx+1                         #aggiornamento della dim massima
                    
                sx-=1
                dx+=1
            
        return stringa_out    
    

