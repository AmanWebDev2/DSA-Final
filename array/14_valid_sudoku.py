def brute(board:list[list[int]]):
    # row validation
    n = len(board)
    for row in range(n):
        st = set()
        for col in range(n):
            if board[row][col] == '.':
                continue

            if board[row][col] in st:
                return False
            
            st.add(board[row][col])
    
    # column validation
    for col in range(n):
        st = set()
        for row in range(n):
            if board[row][col] == '.':
                continue

            if board[row][col] in st:
                return False
            
            st.add(board[row][col])

    return True
