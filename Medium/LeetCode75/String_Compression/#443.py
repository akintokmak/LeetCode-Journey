from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int :
        read = 0
        write = 0
        while read < len(chars):
            count = 0
            current_char = chars[read]
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1
            chars[write] = current_char
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write

slt = Solution()
print(slt.compress(["a", "a", "b", "b", "c", "c", "c"]))