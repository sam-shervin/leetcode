class Solution:
    def myAtoi(self, s: str) -> int:
        # Define constants for 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Trim leading whitespace
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Check for sign
        sign = 1
        index = 0
        if s[0] in ('-', '+'):
            if s[0] == '-':
                sign = -1
            index += 1

        # Step 3: Convert digits
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])

            # Step 4: Handle overflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            index += 1

        return sign * result

    
        