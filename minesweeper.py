# Time Complexity - O(m*n)
# Space complexity - O(m*n)
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        # Time Complexity - O(1) as 8 steps only
        def countMines(x,y):
            result = 0
            for i,j in [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]:
                r,c = x + i, y + j
                if 0 <= r < m and 0 <= c < n and board[r][c] == 'M':
                    result+= 1
            return result


        m = len(board)
        n = len(board[0])
        q = deque()
        # check if first click is M on the board: then reveal it to be X and return board
        r,c = click
        if board[r][c] == 'M':
            board[r][c] = 'X' 
            return board
        else:
            q.append((r,c))
            board[r][c] = 'B' 
            while q:
                x,y = q.popleft()
                count = countMines(x,y)
                if count == 0:
                    # iterate over the neighbors using dirs 
                    for i,j in [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]:
                        r,c = x + i, y + j
                        #  bound condition and board is E then add to q
                        if 0 <= r < m and 0 <= c < n and board[r][c] == 'E':
                            board[r][c] = 'B'
                            q.append((r,c))
                
                else:
                    # update board with no of count 
                    print(r,c) 
                    # if 0 <= r < m and 0 <= c < n:
                    board[x][y] = str(count)
        return board


        
