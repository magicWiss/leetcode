'''
Created on 4 gen 2022
Given a string s, find the length of the longest substring without repeating characters.
@author: Wissel
'''

def longest_sub(s):
    
    #indice esterno
    i=0
    
    #output
    massimo=0
    
    #set di appoggio,memorizza tutti i caratteri che abbiamo visitato
    charSet=set()    
    for j in range(len(s)):                 #per ogni carattere della stringa
        
        while s[j] in charSet:              #se troviamo un duplicato
            
            #rimuoviamo i dal set
            charSet.remove(s[i])
            
            #incrementiamo i
            i+=1
        
        #aggiorno il set
        charSet.add(s[j])
        
        #aggirno il massimo
        
        massimo=max(massimo, j-i+1)          
    return massimo

s1="abcabcbb"
print(s1,"-->",longest_sub(s1))
s2="bbbb"
print(s2,"-->",longest_sub(s2))
s3="pwwkew"
print(s3,"-->",longest_sub(s3))
            
            
