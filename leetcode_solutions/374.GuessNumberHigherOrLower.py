'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #Binary search
        if n==1:
            return 1
        l=0
        r=n
        while l<r:
            m=l+(r-l)//2
            curr_ris=guess(m)      
            #right pick
            if curr_ris==0:
                return m
            #to big
            if curr_ris<0:
                r=m
            elif curr_ris>0:
                l=m+1
        return l
    


        
