MOD_CONSTANT = 10 ** 9 + 7


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        paths_ending_at_cell = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        def dfs(row_index, col_index):
            if paths_ending_at_cell[row_index][col_index] != 0:
                return paths_ending_at_cell[row_index][col_index]
            paths_ending_at_current_cell = 1
            if (
                row_index + 1 < num_rows
                and grid[row_index + 1][col_index] < grid[row_index][col_index]
            ):
                paths_ending_at_current_cell += (
                    dfs(row_index + 1, col_index) % MOD_CONSTANT
                )
            if (
                row_index - 1 >= 0
                and grid[row_index - 1][col_index] < grid[row_index][col_index]
            ):
                paths_ending_at_current_cell += (
                    dfs(row_index - 1, col_index) % MOD_CONSTANT
                )
            if (
                col_index + 1 < num_cols
                and grid[row_index][col_index + 1] < grid[row_index][col_index]
            ):
                paths_ending_at_current_cell += (
                    dfs(row_index, col_index + 1) % MOD_CONSTANT
                )
            if (
                col_index - 1 >= 0
                and grid[row_index][col_index - 1] < grid[row_index][col_index]
            ):
                paths_ending_at_current_cell += (
                    dfs(row_index, col_index - 1) % MOD_CONSTANT
                )
            paths_ending_at_cell[row_index][col_index] = paths_ending_at_current_cell
            return paths_ending_at_current_cell

        return (
            sum(
                dfs(row_index, col_index)
                for row_index in range(num_rows)
                for col_index in range(num_cols)
            )
            % MOD_CONSTANT
        )
