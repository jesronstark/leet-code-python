from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        dict_t = Counter(t)
        required = len(dict_t)
        left, right = 0, 0
        formed = 0
        window_counts = {}
        min_length = float("inf")
        min_window = (0, 0)

        while right < len(s):
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while left <= right and formed == required:
                character = s[left]

                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = (left, right)

                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                left += 1

            right += 1

        return "" if min_length == float("inf") else s[min_window[0]:min_window[1] + 1]
