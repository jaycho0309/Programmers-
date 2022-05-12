def solution(n, times):
    answer = 0
    person = 0
    
    # 심사대에서 심사가 끝날 때 마다의 체크를 위한 list 생성
    times_cp = list(times)
    
    # 각 심사대에서 심사가 끝날 때 마자 person++. n이 되면 종료
    while (person < n):
        m = min(times_cp) # 가장 먼저 심사 끝나는 심사대 결정
        for i in range(len(times_cp)):
            times_cp[i] -= m # 시간 소요
            if times_cp[i] == 0:
                person += 1
                times_cp[i] = times[i] # 심사가 끝난 곳은 새로운 사람을 받음
        answer += m
    return answer
