class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        rowHash = [0] * 9
        colHash = [0] * 9
        gridHash = [0] * 9
        bits = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    grid = i / 3 * 3 + j / 3
                    bit = bits[val]
                    if rowHash[i] & bit == 0:
                        rowHash[i] |= bit
                    else: return False
                    if colHash[j] & bit == 0:
                        colHash[j] |= bit
                    else: return False
                    if gridHash[grid] & bit == 0:
                        gridHash[grid] |= bit
                    else: return False
        return True