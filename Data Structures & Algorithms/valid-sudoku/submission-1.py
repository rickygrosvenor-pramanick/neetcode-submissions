class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_rows = 9
        num_cols = 9

        for row in board:
            num_set = set()
            for slot in row:
                if slot == ".":
                    continue
                if slot.isnumeric():
                    if int(slot) in num_set:
                        return False
                    num_set.add(int(slot))
        
        for i in range(0, num_cols):
            num_set = set()
            for row in board:
                slot = row[i]
                if slot == ".":
                    continue
                if slot.isnumeric():
                    if int(slot) in num_set:
                        return False
                    num_set.add(int(slot))
        
        for row in {0, 3, 6}:
            for col in {0, 3, 6}:
                num_set = set()
                for dr in range(0, 3):
                    for dc in range(0, 3):
                        slot = board[row+dr][col+dc]
                        if slot == ".":
                            continue
                        if slot.isnumeric():
                            if int(slot) in num_set:
                                return False
                            num_set.add(int(slot))
        
        return True
