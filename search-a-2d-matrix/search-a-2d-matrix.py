class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row = 0
        column = len(matrix[0]) - 1

        while column >= 0 and row < len(matrix):
            if matrix[row][column] < target:
                row += 1
            elif matrix[row][column] > target:
                column -= 1
            else:
                return [row, column]