class Solution:

    
            
    def longestCommonPrefix(self, strs) -> str:

        first=strs[0]
        try:
            second=strs[1]

            comm=getSamePrefix(first,second)
        
            for i in range(2,len(strs)):
                curr=getSamePrefix(comm,strs[i])
                if len(comm)>=len(curr):
                    comm=curr
            
            return comm

        except:
            return first

def getSamePrefix(a,b):
        out=''
        for i,j in zip(a,b):

            if i==j:
                out=out+i
            else:
                return out
        return out

def main():
    input=['casco','cascata','casa']

    print(Solution().longestCommonPrefix(input))

if __name__=="__main__":main()


            
        