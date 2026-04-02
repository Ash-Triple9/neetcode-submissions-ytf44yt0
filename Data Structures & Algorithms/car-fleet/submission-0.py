class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        for r in range(len(position)):
            posSpeed.append([position[r], speed[r]])
        posSpeed = sorted(posSpeed)
        stack = []
        if not posSpeed:
            return 0
        for pair in posSpeed:
            while stack:
                prevPairPos, prevPairSpeed = stack[-1][0], stack[-1][1]
                curPairPos, curPairSpeed = pair[0], pair[1]

                print(f"{prevPairPos} {prevPairSpeed}")
                print(f"{curPairPos} {curPairSpeed}")

                curPairFinishTime = (target-curPairPos)/curPairSpeed
                prevPairFinishTime = (target-prevPairPos)/prevPairSpeed



                if curPairFinishTime>=prevPairFinishTime:
                    stack.pop(-1)
                else:
                    break
            stack.append(pair)
        return len(stack)
                
                


                
        