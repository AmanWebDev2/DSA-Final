'''
T.C -> O(9 X 9) + O(9) + O(9) = O(1)
S.C -> O(1)
'''

def isValidSudoku(board: list[list[str]]) -> bool:
    for row in board:
        st = set()
        for val in row:
            if val == '.':
                continue
            if val in st:
                return False
            st.add(val)
    
    for i in range(0,9):
        st = set()
        for j in range(0,9):
            val = board[j][i]
            if val == '.':
                continue
            if val in st:
                return False
            st.add(val)
    
    for sr in range(0,9,3):
        er = sr + 2
        for sc in range(0,9,3):
            ec = sc + 2
            traverse(board,sr,er,sc,ec)
    
    return True
    
        
def traverse(board,sr,er,sc,ec):
    st = set()
    for i in range(sr,er+1):
        for j in range(sc,ec+1):
            val = board[i][j]
            if val == '.':
                continue
            # print(st)
            if val in st:
                print(val)
                return False
            st.add(val)

board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))


