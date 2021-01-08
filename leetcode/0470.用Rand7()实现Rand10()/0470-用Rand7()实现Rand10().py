# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = (rand7()-1)*7+rand7() #1-49
        if num<=40:
            return num%10+1       
        num1 = (num-41)*7+rand7() #1-63
        if num1<=60:
            return num1%10+1
        num2 = (num1-61)*7+rand7() #1-21
        while num2>20:
            num2 = (num1-61)*7+rand7() 
        return num2%10+1
        
        