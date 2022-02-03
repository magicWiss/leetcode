'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''




class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        list_of_words=s.split()

        if len(pattern)!=len(list_of_words):
            return False
        
        #if len(set(list_of_words)!=len(set(p)):return False
        word4let={} #->we could not use this if we create a set from the pattern and a set from the words string a compare lens

        letViewd=set()
        
        for let,word in zip(pattern,list_of_words):

            if word not in word4let and let not in letViewd:
                word4let[word]=let
                letViewd.add(let)
            elif word not in word4let and let in letViewd:
                return False

            else:
                curL=word4let[word]
                if let!=curL :
                    return False
            
        return True

if __name__=="__main__":
    print(Solution().wordPattern("abba","dog cat cat dog"))

        