class Solution:
    def clearDigits(self, s: str) -> str:
        t = []
        for x in list(s):
            if x.isdigit():
                t.pop()
            else:
                t.append(x)
        return ''.join(t)
