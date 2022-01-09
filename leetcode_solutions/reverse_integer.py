#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value 
# to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.


class Solution:
    def reverse(self, x: int) -> int:
        if (x>=(2**31-1) or (x<=-2**31)):
            return 0
        risultato=0                                     #il risultato finale    
        str_associata=str(x)                            #si trasforma l'intero in una stringa cosi da poter iterare
        start=0                                         #verifica che il numero sia positivo
        if(str_associata[0]=='-'):                      #se il primo elemento è un -, allora è negativa
            start=1                                     #memorizzo la negatività
            str_associata=str_associata[1:len(str_associata)+1]     #copio la stringa dal primo all'ultimo numero, escludendo -
        j=len(str_associata)-1
        while j>=0:
            
            risultato=risultato+int(str_associata[j])*(10**j)   #calcolo del risultato
            j-=1
        if start==1:
            risultato= risultato*-1
        
        if risultato>=(2**31-1) or (risultato<=-2**31):
            return 0
        
        return risultato      

def main():
    s=Solution()
    print("10->",s.reverse(10))
    
    print("151->",s.reverse(151))
    
    print(s.reverse(11))
    print(s.reverse(-110))
    print(s.reverse(1410))
    print(s.reverse(-2147483648))
    print(s.reverse(1534236469))


if __name__=="__main__":main()
        