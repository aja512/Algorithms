class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        final_prob = [0 for i in range(target + 1)]
        final_prob[0] = 1
        for i, p in enumerate(prob):
            for j in range(min(i + 1, target), 0, -1):
                final_prob[j] += (final_prob[j - 1] - final_prob[j]) * p
            final_prob[0] *= (1 - p)
        return final_prob[target]
