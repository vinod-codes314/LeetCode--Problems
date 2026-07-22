class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jset=set(jewels)
        c=0
        for stone in stones:
            if stone in jset:
                c+=1
        return c