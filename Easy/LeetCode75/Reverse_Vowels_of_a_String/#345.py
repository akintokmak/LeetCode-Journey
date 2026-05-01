class Solution:
    def reverseVowels(self,s: str) -> str:
        list_s = list(s)
        left = 0
        right = len(s) - 1
        vowels = set("aeiouAEIOU")
        while left < right:
            while left < right and list_s[left] not in vowels:
                left += 1
            while left < right and list_s[right] not in vowels:
                right -= 1

            list_s[left],list_s[right] = list_s[right],list_s[left]

            left += 1
            right -= 1

        return "".join(list_s)

slt = Solution()
print(slt.reverseVowels("IceCreAm"))

