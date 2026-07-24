class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c=0
        ans=0
        for i in range(0,len(s)):
            if s[i] == "R":
                c+=1
            if s[i] == "L":
                c-=1
            if c==0:
                ans+=1

        return ans
                
        