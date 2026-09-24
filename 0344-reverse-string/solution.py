class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def revstr(i: int, j: int) -> None:
            if i >= j:
                return

            s[i], s[j] = s[j], s[i]
            revstr(i + 1, j - 1)

        revstr(0, len(s) - 1)
