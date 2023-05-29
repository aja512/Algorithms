class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        it = iter(s)
        return next((len(t)-i for i, ch in enumerate(t) if ch not in it), 0)
