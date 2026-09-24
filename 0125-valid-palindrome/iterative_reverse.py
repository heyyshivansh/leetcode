class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join([char for char in s if char.isalnum()]).lower()
        revss = clean_s[::-1]

        return revss == clean_s
