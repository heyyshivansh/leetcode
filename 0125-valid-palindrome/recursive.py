class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join([char for char in s if char.isalnum()]).lower()

        def helper(start, end, clean_s):
            if start >= end:
                return True

            if not clean_s[start] == clean_s[end]:
                return False

            return helper(start + 1, end - 1, clean_s)

        return helper(0, len(clean_s) - 1, clean_s)
