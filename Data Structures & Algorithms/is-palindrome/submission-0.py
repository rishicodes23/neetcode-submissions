class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
        print (clean)
        for i in range(len(clean)):
            if clean[i] != clean[len(clean) - 1 - i ]:
                return False
        return True
