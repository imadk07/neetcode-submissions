class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for chr in s:
            if chr in mapping:
                if stack and stack[-1] == mapping[chr]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(chr)
        return True if not stack else False