from math import gcd

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        return str1[0:gcd(len(str1),len(str2))]


slt = Solution()
#case1
print(slt.gcdOfStrings('abcabc','abc'))
#case2
print(slt.gcdOfStrings('ababab','abab'))
#case3
print(slt.gcdOfStrings('leet','code'))
#case4
print(slt.gcdOfStrings('aaaaab','aaa'))

