def solution(m, n, puddles):
    answer = 0
    # m x n 격자 생성
    route = [[0 for _ in range(m)] for _ in range(n)]
    # 가로로 웅덩이가 없을 때 까지 전진할 수 있는 최대 거리
    for i in range(m):
        if [i+1, 1] in puddles:
            break
        route[0][i] = 1
    # 세로로 웅덩이가 없을 때 까지 전진할 수 있는 최대 거리
    for i in range(n):
        if [1, i+1] in puddles:
            break
        route[i][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            if [j+1, i+1] in puddles: # 우물 좌표는 1씩 더해짐을 주의
                route[i][j] = 0  # 우물 격자 좌표와 배열 좌표 반대임을 주의
            else:
                route[i][j] = route[i-1][j] + route[i][j-1]
    return route[n-1][m-1] % 1000000007
