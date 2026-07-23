class Solution(object):
    def isPalindrome(self, s):
        n = ""
        for ch in s:
            if ch.isalnum():
                n += ch.lower()
        return n== n[::-1]
        