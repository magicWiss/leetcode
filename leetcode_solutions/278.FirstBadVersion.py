'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version
 of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following 
ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find 
the first bad version. You should minimize the number of calls to the API.

'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        while True:

            versionCorr=isBadVersion(n)

            if versionCorr:
                if not isBadVersion(n-1):
                    return n
                
                if isBadVersion(n-1):
                    n=n//2
            
            if not versionCorr:

                if  isBadVersion(n+1):
                    return n+1
                if not isBadVersion(n+1):
                    n=n+2

            
