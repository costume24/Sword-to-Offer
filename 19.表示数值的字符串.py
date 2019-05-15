from exeTime import exeTime
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        simbol=['+','-']
        ex=['E','e']
        for item in s:
            