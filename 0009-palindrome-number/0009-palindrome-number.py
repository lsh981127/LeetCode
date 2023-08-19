class Solution(object):
    def isPalindrome(self, x):
        
        strlist = list(str(x))
        
        reversestr = list(reversed(strlist))
        if strlist == reversestr:
            return True
        else:
            return False
        
#         i = 0
#         while i == len(strlist):
#             if strlist[i] != reversestr[i]:
#                 return False
#             i += 1
        
#         return True
        
        