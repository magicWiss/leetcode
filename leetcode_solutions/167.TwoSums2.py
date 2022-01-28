'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a 
specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''

class Solution:
    def twoSum(self, numbers, target: int):

        values=dict()
        #creating values
        for i in range(0,len(numbers)):

            if numbers[i] not in values:
               
                values[numbers[i]]=i+1
            else:
                lst=[]
                lst.append(values[numbers[i]])
                lst.append(i+1)
                values[numbers[i]]=lst

        #finding pairs
        out=[]
        for k,v in values.items():

            tofind=target-k
           
            if (tofind in values):
                if tofind==k:
                        return values[k]
                if v!=values[tofind]:
                    return [min(values[k],values[tofind]),max(values[k],values[tofind])]
        return out
        

if __name__=="__main__":

    Solution().twoSum([0,0,3,4],0)
        