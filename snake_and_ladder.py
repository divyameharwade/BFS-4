
# TIme complexity - O(n*n)
# space complexity - O(n*n)
class Solution:

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        array = [0]* ((n*n)+1)
        idx = 1
        c = 0
        r = n-1
        flag = True
        while idx < len(array):
            array[idx] = board[r][c]
            idx += 1
            #new rc
            if flag:
                c += 1
                if c == n:
                    flag = False
                    r -= 1
                    c -= 1
            else:
                c -= 1
                if c < 0:
                    flag = True
                    r -= 1
                    c += 1 # because we have gone outside the bounds
        q = deque([1])
        visited = set([1])
        count = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur >= n*n: return count
                for j in range(1,7,1): # roll the dice
                    child = cur + j
                    if (child >= n*n) or (array[child] >= n*n): return count + 1

                    if array[child] == -1:
                        if child not in visited:
                            q.append(child)
                            visited.add(child)
                    else:
                        if array[child] not in visited:
                            q.append(array[child])
                            visited.add(array[child])

            count+=1
        return count if count >= n*n else -1
