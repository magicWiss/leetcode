class Solution:
    def removeDuplicates(self, nums) -> int:

        if not nums:
            return 0

        i=0

        for j in range(1,len(nums)):
            print("indici i=",i,"j=",j)
            if nums[i]!=nums[j]:
                
                print("prima:",nums)
               
                print("durante:",nums)
               
                print("dopo:",nums)
                i+=1
                
                nums[i]=nums[j]
               
                
                
        print (nums[0:i+1])
        return i+1 

def main():

    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])) 

if __name__=="__main__":main()