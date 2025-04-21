class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_len = 0

        # Left to Right
        for c in s:
            if c == '(': left += 1
            else: right += 1
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0

        left = right = 0
        # Right to Left
        for c in reversed(s):
            if c == ')': right += 1
            else: left += 1
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0

        return max_len
