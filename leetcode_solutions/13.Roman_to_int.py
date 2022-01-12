#Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:

        trad=dict()
        trad={
            'I':             1,
            'V':             5,
            'X':             10,
            'L':             50,
            'C':             100,
            'D':             500,
            'M':             1000}
        out=0

        for i in range(len(s)-1):
            if trad[s[i]]>=trad[s[i+1]]:
                out+=trad[s[i]]
            else:
                out-=trad[s[i]]
        out+=trad[s[len(s)-1]]
        return out
        