class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers = {x for x in range(1, 10)}
        # row check
        for i in range(0, 9):
            row_set = set()
            for j in range(0, 9):
                square = board[i][j]
                if square == ".":
                    continue
                else:
                    if not square.isnumeric() or int(square) not in numbers or int(square) in row_set:
                        return False
                    else:
                        row_set.add(int(square))

        
        # column check
        for j in range(0, 9):
            col_set = set()
            for i in range(0, 9):
                square = board[i][j]
                if square == ".":
                    continue
                else:
                    if not square.isnumeric() or int(square) not in numbers or int(square) in col_set:
                        return False
                    else:
                        col_set.add(int(square))
        
        # 3x3 Box Check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box_set = set()
                for k in range(0, 3):
                    for l in range(0, 3):
                        square = board[i + k][j + l]
                        if square == ".":
                            continue
                        else:
                            if not square.isnumeric() or int(square) not in numbers or int(square) in sub_box_set:
                                return False
                            else:
                                sub_box_set.add(int(square))
        
        return True
        


                