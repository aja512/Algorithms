/**
 * Time Complexity: O(k * n_edges * log(n))
 * Space Complexity: O(n + n_edges)
 * where `n_edges` is the length of the vector `edges`
 */
class Solution {
 public:
  int shortestPathWithHops(const int n,
                           const vector<vector<int>> &edges,
                           const int s,
                           const int d,
                           const int k) {
    /**
     * {
     *   the sum of weight from the source node to the current node,
     *   the current node,
     *   the number of hopped-over edges from the source node to the current node
     * }
     */
    using pq_node_t = tuple<int, int, int>;
    constexpr int hop_deltas[] = {0, 1};
    constexpr int node1_i = 0;
    constexpr int node2_i = 1;
    constexpr int weight_i = 2;
    vector<pair<int, int>> graph[n];   // node -> {{next node1, weight1}, {next node2, weight2} ...}
    for (const vector<int> &edge : edges) {
      graph[edge[node1_i]].emplace_back(edge[node2_i], edge[weight_i]);
      graph[edge[node2_i]].emplace_back(edge[node1_i], edge[weight_i]);
    }
    
    int hops[n];
    fill(hops, hops + n, k + 1);
    priority_queue<pq_node_t, vector<pq_node_t>, greater<>> pq;
    pq.emplace(0, s, 0);
    while (!pq.empty()) {
      const auto [weight, node, hop] = pq.top();
      pq.pop();
      if (hop >= hops[node]) {
        continue;
      }
      hops[node] = hop;
      
      if (node == d) {
        return weight;
      }
      
      for (const auto [next_node, delta_weight] : graph[node]) {
        for (const int hop_delta : hop_deltas) {
          const int next_hop = hop + hop_delta;
          if (next_hop >= hops[next_node]) {
            continue;
          }
          const int next_weight = weight + (hop_delta == 0 ? delta_weight : 0);
          pq.emplace(next_weight, next_node, next_hop);
        }
      }
    }
    throw "impossible path";
  }
};
