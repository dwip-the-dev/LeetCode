class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Map: character → its most recent index
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # If we've seen this char AND it's inside current window
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1  # Jump left past the duplicate
            
            char_index[char] = right  # Update char's latest position
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        
        return max_length