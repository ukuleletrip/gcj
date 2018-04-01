class ANewHope():
    def count(self, firstWeek, lastWeek, D):
        if firstWeek == lastWeek:
            return 1

        answer = 1
        p_cond = {}
        for i in range(len(lastWeek)):
            p_cond[lastWeek[i]] = i

        while True:
            cond = {}
            for t,v in sorted(p_cond.items(), key=lambda x:x[1]):
                limit = len(firstWeek)-D+p_cond[t]
                if limit < len(firstWeek)-1:
                    cond[t] = limit
                else:
                    break

            for t in cond:
                if firstWeek.index(t) > cond[t]:
                    break
            else:
                return answer+1
            answer += 1
            p_cond = cond

a = ANewHope()

