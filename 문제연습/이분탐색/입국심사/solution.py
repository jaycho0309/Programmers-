def solution(n, times):
    answer = 0
    # 오름차순으로 정렬
    times = sorted(times)
    
    start, end = 0, times[-1] * n # 최소 시간과 최대 걸릴 수 있는 시간 지정
    while start < end:
        # 총 걸린시간 임의 설정
        mid = (start + end) // 2
        person = 0
        for time in times:
            person += mid // time
        # n 보다 적게 심사됨. 더 심사해야함. mid를 늘려야함
        if person < n:
            start = mid + 1
        # 반대
        else:
            end = mid
    return end
