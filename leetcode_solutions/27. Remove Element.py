
'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


'''


class Solution:
    def removeElement(self, nums, val) -> int:

        i=0

        for j in range(0,len(nums)):

            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
                
                
                
             
        return i

def main():

    input=[0,1,2,2,3,0,4,2]

    s=Solution().removeElement(input,2)

    print(input[0:s+1])

if __name__=="__main__":main()


        