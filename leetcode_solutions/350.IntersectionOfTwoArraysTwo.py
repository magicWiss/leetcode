'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''
class Solution:
    def intersect(self, nums1, nums2):

        out=[]
        i,j=0,0
        nums1.sort()
        nums2.sort()
        while i <len(nums1) and j<len(nums2):

            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            elif nums1[i]==nums2[j]:
                out.append(nums1[i])
                i+=1
                j+=1
        return out


        