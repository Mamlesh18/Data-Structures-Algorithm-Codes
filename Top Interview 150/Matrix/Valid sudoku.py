from collections import defaultdict
def valid(matrix):
    if not matrix:
        return False
    rows = defaultdict(set)
    cols = defaultdict(set)
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            if matrix[i][j] == '.':
                continue
            if matrix[i][j] in rows[i] or matrix[i][j] in cols[j]:
                return False
            rows[i].add(matrix[i][j])
            cols[j].add(matrix[i][j])

    return True

matrix = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(valid(matrix))