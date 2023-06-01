/**
 * @param {number[]} prob
 * @param {number} target
 * @return {number}
 */
function probabilityOfHeads(prob, target) {
    const n = prob.length,
        dp = new Array(target + 1).fill(0)
    dp[0] = 1.0

    for (let i = 0; i < n; ++i)
        for (let j = Math.min(i + 1, target); j >= 0; --j)
            dp[j] = dp[j] * (1 - prob[i]) + (j > 0 ? dp[j - 1] : 0) * prob[i]
    return dp[target]
}
