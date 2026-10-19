class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        i = 1
        output = [1, 1]
        while i < rowIndex:
            temp = []
            for i in range(1, len(output)):
                temp.append(output[i-1] + output[i])
            output = [1] + temp + [1]
            i += 1
        return output
