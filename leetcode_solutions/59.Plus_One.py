'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

'''
class Solution:
    def plusOne(self, digits):

        n=len(digits)
        output=[0 for i in range (len(digits))]

        self.add_one(digits,output,n-1,1)
        return output
    def add_one(self,inp,out,n,resto):


            if resto==0:
                out[n]=inp[n]

            if resto==1:
                if inp[n]==9:
                    out[n]=0
                    resto=1
                else:
                    out[n]=inp[n]+1
                    resto=0
            if n==0 and resto==1 and inp[n]==9:
                out[n]=0
                out.insert(0,1)
            if n==0:
                return 

            self.add_one(inp,out,n-1,resto)

def main():

    print(Solution().plusOne([8,9,9]))

if __name__=="__main__":main()
        