class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s="abcdefghijklmnopqrstuvwxyz"
        return len(set(sentence)) == 26