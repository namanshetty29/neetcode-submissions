class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count_1 = {}
        letter_count_2 = {}
        for letter in s.lower():
            letter_count_1[letter] = letter_count_1.get(letter, 0) + 1
        for letter in t.lower():
            letter_count_2[letter] = letter_count_2.get(letter, 0) + 1
        if letter_count_1==letter_count_2:
            return True
        return False