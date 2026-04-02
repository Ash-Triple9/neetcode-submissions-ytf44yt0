class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rowL= 0
        rowR = len(matrix)-1

        while rowL<=rowR:
            rowM = (rowL+rowR)//2
            if target<=matrix[rowM][-1] and target>=matrix[rowM][0]:
                ## Found the row we need to operate in
                colL =0
                colR = len(matrix[rowM])-1
                while colL<=colR:
                    colM = (colL+colR)//2
                    if target == matrix[rowM][colM]:
                        return True
                    elif target> matrix[rowM][colM]:
                        colL = colM+1
                    elif target<matrix[rowM][colM]:
                        colR = colM-1
                break

            elif target>matrix[rowM][-1]:
                ## Move left pointer
                rowL = rowM +1

            elif target<matrix[rowM][0]:
                ## Move right pointer
                rowR = rowM-1 
        return False
        