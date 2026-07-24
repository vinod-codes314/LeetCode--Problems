class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for ch in s:
            if ch.isalnum():
                ans+=ch
        ans=ans.lower()
        rans=ans[::-1]
        return ans == rans