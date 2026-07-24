class Solution:
    def judgeCircle(self, moves: str) -> bool:
        lc=rc=uc=dc=0
        for i in range(0,len(moves)):
            if moves[i]=="L":
                lc+=1
            if moves[i]=="R":
                rc+=1
            if moves[i]=="U":
                uc+=1
            if moves[i]=="D":
                dc+=1
        return lc==rc and uc==dc
        