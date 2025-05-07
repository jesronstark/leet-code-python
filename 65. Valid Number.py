
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Define the regular expression pattern
        number_pattern = re.compile(r"""
            ^\s*                # Leading whitespace
            [+-]?               # Optional sign
            (                   # Main number part:
                (\d+(\.\d*)?)   # Integer or decimal (e.g., 123, 123. or 123.45)
                |               # or
                (\.\d+)         # Decimal without leading digits (e.g., .123)
            )
            ([eE][+-]?\d+)?     # Optional exponent part (e.g., e10, E-2)
            \s*$                # Trailing whitespace
        """, re.VERBOSE)

        # Use fullmatch to ensure the entire string matches the pattern
        return re.fullmatch(number_pattern, s) is not None
solution = Solution()

print(solution.isNumber("123"))        # True
print(solution.isNumber(" 123.45 "))   # True
print(solution.isNumber("-123.45e6"))  # True
print(solution.isNumber("1e-10"))      # True
print(solution.isNumber("abc"))        # False
print(solution.isNumber("1a"))         # False
print(solution.isNumber("e3"))         # False

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Define the regular expression pattern
        number_pattern = re.compile(r"""
            ^\s*                # Leading whitespace
            [+-]?               # Optional sign
            (                   # Main number part:
                (\d+(\.\d*)?)   # Integer or decimal (e.g., 123, 123. or 123.45)
                |               # or
                (\.\d+)         # Decimal without leading digits (e.g., .123)
            )
            ([eE][+-]?\d+)?     # Optional exponent part (e.g., e10, E-2)
            \s*$                # Trailing whitespace
        """, re.VERBOSE)

        # Use fullmatch to ensure the entire string matches the pattern
        return re.fullmatch(number_pattern, s) is not None
solution = Solution()

print(solution.isNumber("123"))        # True
print(solution.isNumber(" 123.45 "))   # True
print(solution.isNumber("-123.45e6"))  # True
print(solution.isNumber("1e-10"))      # True
print(solution.isNumber("abc"))        # False
print(solution.isNumber("1a"))         # False
print(solution.isNumber("e3"))         # False
