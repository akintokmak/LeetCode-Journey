class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split()
        list_s.reverse()
        return ' '.join(list_s)

slt = Solution()
print(slt.reverseWords("the sky is blue"))


"""Manual Search"""
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         list_s = s.split()
#         left = 0
#         right = len(list_s) - 1
#         while left < right:
#             list_s[left], list_s[right] = list_s[right], list_s[left]
#             left += 1
#             right -= 1
#
#         return ' '.join(list_s)
#
#
# slt = Solution()
# print(slt.reverseWords("the sky is blue"))
