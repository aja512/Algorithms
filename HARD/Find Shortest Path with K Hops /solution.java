class Solution {
    public int shortestPathWithHops(int n, int[][] edges, int s, int d, int k) {
        List<ArrayList<int[]>> al = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            al.add(new ArrayList<>());
        }

        for (int[] e : edges) {
            al.get(e[0]).add(new int[]{e[1], e[2]});
            al.get(e[1]).add(new int[]{e[0], e[2]});
        }

        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        }
        dp[s][k] = 0;

        Deque<int[]> deque = new LinkedList<>();
        deque.offer(new int[]{s, k, 0});

        while (!deque.isEmpty()) {
            int[] current = deque.poll();
            int i = current[0];
            int count = current[1];
            int path = current[2];

            if (dp[i][count] != path || i == d) {
                continue;
            }

            for (int[] neighbor : al.get(i)) {
                int j = neighbor[0];
                int w = neighbor[1];

                if (dp[j][count] > dp[i][count] + w) {
                    dp[j][count] = dp[i][count] + w;
                    deque.offer(new int[]{j, count, dp[j][count]});
                    if (count > 0) {
                        dp[j][count - 1] = Math.min(dp[j][count - 1], dp[j][count]);
                    }
                }

                if (count > 0 && dp[j][count - 1] > dp[i][count]) {
                    dp[j][count - 1] = dp[i][count];
                    deque.offer(new int[]{j, count - 1, dp[j][count - 1]});
                    if (count - 1 > 0) {
                        dp[j][count - 2] = Math.min(dp[j][count - 2], dp[j][count - 1]);
                    }
                }
            }
        }

        int minPath = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            minPath = Math.min(minPath, dp[d][i]);
        }

        return minPath;
    }
}
