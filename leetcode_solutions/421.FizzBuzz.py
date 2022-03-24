'''
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
'''
class Solution(object):
    def fizzBuzz(self, n):
        return [str(i)*(i%3!=0 and i%5!=0)+"Fizz"*(i%3==0)+"Buzz"*(i%5==0) for i in range(1,n+1)]