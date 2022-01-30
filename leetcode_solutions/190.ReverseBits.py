'''
Reverse bits of a given 32 bits unsigned integer.
'''
class Solution:
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)      #shift di un bit e and logico tra il numero n e 1
            n >>= 1
        return ans


        

   
        