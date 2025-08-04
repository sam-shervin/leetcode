class Solution:
    def setZeroes(self, matrix):
        first_row_zero = False
        first_col_zero = False

        # Check if first row has a zero
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check if first column has a zero
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Use first row and column to mark zeros
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on markers
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0

        # Zero out first row if needed
        if first_row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        # Zero out first column if needed
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
