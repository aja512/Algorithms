class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(list) # Mapping character count to list of Anagrams

        for s in strs:
            count = [0] * 26 # Counting through the alphabets a-z and how many each alphabet has
            for c in s:
                count[ord(c) - ord("a")] += 1
            answer[tuple(count)].append(s)  # ASCII Value addition
        return answer.values()
