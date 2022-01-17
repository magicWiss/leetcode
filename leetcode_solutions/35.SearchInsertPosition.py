'''Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''


class Solution:
    def searchInsert(self, nums, target: int) -> int:

        #indice inferiore
        inf=0
        #indice superiore
        sup=len(nums)-1
        #diff
        min=1000000         #numer abbastanza grande

        #torovato
        trovato=False

        index=0

        while inf<=sup:
            medio=(inf+sup)//2
            print("elemento,",nums[medio])

            #caso 1->trovato la soluzione
            if nums[medio]==target:
                return medio

            else:
                #prendo il valore medio e vedo la differenza
                diff=target-nums[medio]
                if min>abs(diff):
                    if diff>0:
                        index=medio+1
                    else:
                        index=medio
                    min=abs(diff)
                
                #andiamo avanti con la ricerca
                if nums[medio]<target:
                    inf=medio+1

                else:
                    sup=medio-1
        return index

def main():

    s=Solution().searchInsert([1,3,5,6],2)

if __name__=="__main__": main()

        
        
        
    