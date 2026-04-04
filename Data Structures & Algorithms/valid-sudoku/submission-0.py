class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_rows = 9
        num_cols = 9

        # row check
        for row in board:
            check_set = set()
            for slot in row:
                if slot == ".":
                    continue
                if int(slot) in check_set:
                    return False
                else:
                    check_set.add(int(slot))
        
        # col check
        for i in range(0, num_cols):
            check_set = set()
            for row in board:
                slot = row[i]
                if slot == ".":
                    continue
                if int(slot) in check_set:
                    return False
                else:
                    check_set.add(int(slot))
        
        # check third condition, 3x3 boxes
        for box_row in (0, 3, 6):
            for box_col in (0, 3, 6):
                check_set = set()
                for dr in range(3):
                    for dc in range(3):
                        slot = board[box_row + dr][box_col + dc]
                        if slot == ".":
                            continue
                        if int(slot) in check_set:
                            return False
                        else:
                            check_set.add(int(slot))
                        
        return True
