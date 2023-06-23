class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0]) 
        count = Counter(sum(board, []))
        # count of a LETTER in word is Greater than count of it being in board
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False  
        # if count of 1st letter of Word(A) is Greater than that of Last One in Board(B). 
        # Reverse Search the word then search as less case will be searched.
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]      


        edges = {}
        q = []
        m, n = len(board), len(board[0])
        for i in range(m):
            edges[(i, -1)] = True
            edges[(i, n)] = True
        for j in range(n):
            edges[(-1, j)] = True
            edges[(m, j)] = True

        for x in range(len(board)):
            for y in range(len(board[0])):
                if word[0] == board[x][y]:
                    q.append((x, y, 0, {(x, y) : True}))
                    while len(q) > 0:
                        curr_x, curr_y, pos, seen = q.pop()
                        #print(curr_x, curr_y, pos)
                        if pos == len(word) - 1:
                            return True
                        candidates = [(curr_x + 1, curr_y), (curr_x - 1, curr_y), (curr_x, curr_y + 1), (curr_x, curr_y - 1)]
                        for next_x, next_y in candidates:
                            if (next_x, next_y) not in seen and (next_x, next_y) not in edges and board[next_x][next_y] == word[pos + 1]:
                                nextSeen = seen.copy()
                                nextSeen[(next_x, next_y)] = True
                                q.append((next_x, next_y, pos + 1, nextSeen))
        return False
