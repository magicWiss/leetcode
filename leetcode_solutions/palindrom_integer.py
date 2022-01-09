#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward.

#For example, 121 is a palindrome while 123 is not.

class Solution:
    def check_ric(self,i,j,out,n,string):
        if (i>=n and j<0) :
            return out
        if string[i]!=string[j]:
            out=out and False
            return out
        return self.check_ric(i+1,j-1,out,n,string)
    def check(self,x):
        string=str(x)
        n=len(string)
        i=j=n//2
        return self.check_ric(i,j,True,n,string)
    def check_even(self,x):
        out=True
        string=str(x)
        n=len(string)
        i,j=n//2,n//2-1         #i iteratore di destra, j di sinitra

        while i<n and j>=0:
            if string[i]!=string[j]:
                return False
            i+=1
            j-=1
        return out
        
    def isPalindrome(self, x: int) -> bool:
        #condizioni iniziali
        if x<0:
            return False
        #soluzione di verifica dal centro
        if len(str(x))%2==0:                # se è pari allora ha due contatori inizialmente diversi
            return self.check_even(x)
        
        return self.check(x)                     #altrimenti i contatori sono ugualiu

        

def main():
    print("1243->",Solution().isPalindrome(1234))
    print("1221->",Solution().isPalindrome(1221))
    print("-121->",Solution().isPalindrome(-121))
    print("1235321->",Solution().isPalindrome(1235321))


if __name__=="__main__":main()
