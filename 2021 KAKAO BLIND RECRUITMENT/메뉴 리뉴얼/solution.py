import itertools

def solution(orders, course):
    answer = []
    k = ''
    for c in course:
        dict = {}
        for order in orders:
            combs = list(itertools.combinations(order, c))
            for comb in combs:
                comb = list(comb)
                comb.sort()
                for com in comb:
                    k += com
                if k not in dict:
                    dict[k] = 1
                else:
                    dict[k] += 1
                k = ''
        temp = [key for key,v in dict.items() if v >= 2 and max(dict.values()) == v]
        answer.extend(temp)
    answer.sort()
    return answer
