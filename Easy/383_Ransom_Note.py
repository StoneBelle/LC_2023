class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        m = list(magazine)
        for letter in ransomNote:
            if letter in m:
                m.remove(letter)
            else:
                return False
        return True
