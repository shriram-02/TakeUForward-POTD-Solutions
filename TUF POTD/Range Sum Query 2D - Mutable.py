class NumMatrix(object):

    def __init__(self, matrix):
        self.m = len(matrix)
        self.n = len(matrix[0]) if self.m else 0

        self.matrix = [row[:] for row in matrix]
        self.bit = [[0] * (self.n + 1)
                    for _ in range(self.m + 1)]

        for i in range(self.m):
            for j in range(self.n):
                self._add(i, j, self.matrix[i][j])

    def _add(self, row, col, delta):
        i = row + 1

        while i <= self.m:
            j = col + 1

            while j <= self.n:
                self.bit[i][j] += delta
                j += j & -j

            i += i & -i

    def _prefixSum(self, row, col):
        total = 0
        i = row + 1

        while i > 0:
            j = col + 1

            while j > 0:
                total += self.bit[i][j]
                j -= j & -j

            i -= i & -i

        return total

    def update(self, row, col, val):
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self._add(row, col, delta)

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self._prefixSum(row2, col2)
            - self._prefixSum(row1 - 1, col2)
            - self._prefixSum(row2, col1 - 1)
            + self._prefixSum(row1 - 1, col1 - 1)
        )