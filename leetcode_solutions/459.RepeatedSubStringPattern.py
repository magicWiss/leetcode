'''
Given a string s, check if it can be constructed by taking a 
substring of it and appending multiple copies of the substring together.
Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false
'''


'''First char of input string is first char of repeated substring
Last char of input string is last char of repeated substring
Let S1 = S + S (where S in input string)
Remove 1 and last char of S1. Let this be S2
If S exists in S2 then return true else false
Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]'''
class Solution:
    def repeatedSubstringPattern(self, str):

        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False
            
        ss = (str + str)[1:-1]
        return ss.find(str) != -1

'''
I would try to propose a more strict proof idea:
It's obvious that valid string will be captured by this algorithm, but why invalid one return false is not intuitive.
From the algorithm, we can conclude that S satisfies that s = AB = BA (by AB, I mean s = the concatenation of A and B).
What I want to prove is if AB = BA, then there is a D such that A = n*D, B = m*D
Suppose len(A) = a, len(B) = b. Two cases:

If a = b or a = 1 or b = 1, the problem is trivial.
Without loss of generality, we could suppose that a < b.
According to AB = BA, we have A = B[1~a], which means that B = AC.
Then AB = BA ==> AAC = ACA and the problem size has been reduced from (a, b) to (a, b-a): AC = CA.
In the end, it will be reduced to one of the case in (1). Thus the problem is solved.
'''
if __name__=="__main__":
    print(Solution().repeatedSubstringPattern("abaababaab"))