#
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#

# @lc code=start
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:


        ## bfs: has runtime limit
        # def isValid(new_r, new_c):
        #     return new_r < N and new_r >= 0 and new_c < N and new_c >= 0

        # if N == 0:
        #     return 0
        # if K == 0: 
        #     return 1
        # moves = [(-1,-2), (-2, -1), (1, 2), (2, 1), (-2, 1), (-1, 2), (2, -1), (1, -2)]
        # queue = collections.deque()
        # queue.append((r, c))
        # count = 0

        # while(queue and count < K):
        #     count += 1
        #     for _ in range(len(queue)):
        #         (row, col) = queue.popleft()
        #         for (r_inc, c_inc) in moves:
        #             new_r = row + r_inc
        #             new_c = col + c_inc
        #             if not isValid(new_r, new_c):
        #                 continue
        #             queue.append((new_r, new_c)) 
        
        # return len(queue) / (8 ** K)
         
        # def isValid(new_r, new_c):
        #     return new_r < N and new_r >= 0 and new_c < N and new_c >= 0






        ## dfs: has runtime limit
        # if N == 0:
        #     return 0
        # moves = [(-1,-2), (-2, -1), (1, 2), (2, 1), (-2, 1), (-1, 2), (2, -1), (1, -2)]
        
        # def dfs(step, r, c, memo):

        #     if (step, r, c) in memo: 
        #         return memo[(step, r, c)]

        #     if step == K: 
        #         return 1

        #     prob = 0
            
        #     for (r_inc, c_inc) in moves:
        #         new_r = r + r_inc
        #         new_c = c + c_inc
        #         if not isValid(new_r, new_c):
        #             continue
        #         prob += dfs(step+1, new_r, new_c, memo)
            
        #     memo[(step, r, c)] = prob
        
        #     return prob

        # return dfs(0, r, c, {}) / (8 ** K) 



        ## dfs with cache

        moves = [(-1,-2), (-2, -1), (1, 2), (2, 1), (-2, 1), (-1, 2), (2, -1), (1, -2)]

        @functools.cache
        def dfs(move, r, c):
            if r < 0 or r >= N or c < 0 or c >= N:
                return 0
            
            if move == K:
                return 1
            
            p = 0
            for dr, dc in moves:
                p += dfs(move + 1, r + dr, c + dc)
            return p
        return dfs(0, r, c) / (8 ** K)
# @lc code=end

