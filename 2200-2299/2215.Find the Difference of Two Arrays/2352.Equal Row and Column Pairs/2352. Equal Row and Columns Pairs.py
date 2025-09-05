class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        columns = {}
        rows = {}
        n = len(grid)
        word_row = ""
        word_col = ""
        result = 0
        for i in range(n):
            for j in range(n):
                word_row += str(grid[i][j]) + ","  
                word_col += str(grid[j][i]) + ","  
            columns[word_col] = columns.get(word_col, 0) + 1
            rows[word_row] = rows.get(word_row, 0) + 1
            word_row = ""
            word_col = ""

        for key in columns.keys():
            if key in rows:
                result += rows[key] * columns[key]

        return result