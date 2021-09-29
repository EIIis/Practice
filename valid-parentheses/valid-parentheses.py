class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
        else:
            stack = []

            for char in s:
                if (char == '{') or (char == '[') or (char == '('):
                    stack.append(char)
                else:
                    if len(stack) == 0:
                        return False
                    else:
                        if char == '}':
                            if stack[-1] == '{':
                                stack.pop()
                            else:
                                return False
                        elif char == ']':
                            if stack[-1] == '[':
                                stack.pop()
                            else:
                                return False
                        else:
                            if stack[-1] == '(':
                                stack.pop()
                            else:
                                return False
            if len(stack) > 0:
                return False
            return True