class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])


        def find_row(matrix: List[List[int]], target, a, b):
            if a > b:
                return None

            mid = (a + b) // 2

            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                return mid
            elif matrix[mid][0] > target:
                return find_row(matrix, target, a, mid - 1)
            elif matrix[mid][n - 1] < target:
                return find_row(matrix, target, mid + 1, b)
                
        row = find_row(matrix, target, 0, m - 1)
        if row is None:
            return False

        def binSearch(lst: List[int], c, d, target):
            if c > d:
                return False
            
            if c == d and lst[c] == target:
                return True
            
            mid = (c + d) // 2

            if lst[mid] == target:
                return True
            elif lst[mid] > target:
                return binSearch(lst, c, mid - 1, target)
            else:
                return binSearch(lst, mid + 1, d, target)
        
        found = binSearch(matrix[row], 0, n - 1, target)

        return found
            
            

        