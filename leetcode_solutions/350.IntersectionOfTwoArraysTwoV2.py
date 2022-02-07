'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Suppose that nums1 or nums2 has a lenght much greather then the other
Condition: len(nums1||nums2) >>>>>>>len( nums2||nums1)

The algo is much slower when working with sizes of inputs pretty much simular
'''
class Solution:
    def intersect(self, nums1, nums2):

        out=[]
        #creating a hash map with overflow list
        ovFlow_map={}
        #getting the max array and min array
        if len(nums1)>len(nums2):
            min=nums1
            max=nums2
        else:
            min=nums2
            max=nums1
        
        #populating the ovFlow_map
        for i in range(0,len(min)):
            if min[i] not in ovFlow_map:
                ovFlow_map[min[i]]=[]
            ovFlow_map[min[i]].append(i)
            

        #navigating the max list and poping the overflow list in the map
        for i in max:
            if i in ovFlow_map:
                out.append(i)
                ovFlow_map[i].pop(0)
                #we check if the entry has a non empty list
                if len(ovFlow_map[i])==0:
                    #delete the list
                    del ovFlow_map[i]
        return out



        