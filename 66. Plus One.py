class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Initialize the carry to 1 (since we are adding one)
        carry = 1
        
        # Process each digit starting from the end
        for i in range(len(digits) - 1, -1, -1):
            new_digit = digits[i] + carry
            digits[i] = new_digit % 10  # Update the digit
            carry = new_digit // 10     # Update the carry
            
            # If there's no carry left, we can return the result early
            if carry == 0:
                return digits
        
        # If there's still a carry after processing all digits, insert it at the beginning
        if carry:
            digits.insert(0, carry)
        
        return digits
