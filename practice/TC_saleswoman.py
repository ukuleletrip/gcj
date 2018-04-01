

class Saleswoman():
    def minMoves(self, pos, delta):
        answer = 0
        item = 0
        first_deposit = -1
        deposit = 0
        for i in range(len(pos)):
            if delta[i] >= 0:
                item += delta[i]
                if deposit and item >= deposit:
                    answer += (pos[i]-pos[first_deposit])*2
                    first_deposit = -1
                    item -= deposit
                    deposit = 0
            else:
                if item+delta[i] >= 0:
                    item += delta[i]
                else:
                    deposit += -(item+delta[i])
                    if first_deposit < 0:
                        first_deposit = i
        return answer + pos[-1]
