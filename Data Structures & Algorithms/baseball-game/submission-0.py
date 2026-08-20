class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        sum = 0
        for operation in operations:
            if operation == 'C':
                old = scores.pop()
                sum -= old
            elif operation == '+':
                new = scores[-1] + scores[-2]
                scores.append(new)
                sum += new
            elif operation == 'D':
                new = scores[-1]*2
                scores.append(new)
                sum += new
            else:
                scores.append(int(operation))
                sum += int(operation)
        return sum