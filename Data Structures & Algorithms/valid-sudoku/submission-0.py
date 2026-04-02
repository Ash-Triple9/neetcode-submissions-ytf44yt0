class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            rowNums = {}
            colNums = {}
            for j in range(len(board[i])):

                if not board[i][j]==".":
                    rowNum = int(board[i][j])
                    rowNums[rowNum]= 1 + rowNums.get(rowNum,0)
                    if rowNums[rowNum]>1:
                        return False

                if not board[j][i]==".":
                    colNum = int(board[j][i])
                    colNums[colNum] = 1+ colNums.get(colNum,0)
                    if colNums[colNum]>1:
                        return False
        r=0
        c=0
        while r < 6:
            subBox = {}
            for i in range(0,3):
                for j in range(0,3):
                    if not board[i+r][j+c]==".":
                        num = int(board[i+r][j+c])
                        subBox[num]= 1+ subBox.get(num,0)
                        if subBox[num]>1:
                            return False
            c+=3
            if c > 6:
                c = 0
                r+=3
                
        return True
            

        
                    
