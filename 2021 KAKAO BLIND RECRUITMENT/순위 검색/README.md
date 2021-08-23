- 시간초과 때문에 dict에 다 넣고 이진검색으로 찾아야 함
- itertools 보다 for문 돌면서 dict 넣는게 편함
- 이진탐색
    - 정렬된 배열에서 탐색 범위를 절반씩 좁혀가며 데이터 탐색 O(logN)
    -   l = 0  
        r = len(pool)  
        mid = 0  
        while l < r:  
            mid = (r+l)//2 # 홀수면 가운데, 짝수면 가운데에서 오른쪽  
            if pool[mid] >= target: # 타겟을 넘었으면 r을 타겟으로 땡김  
                r = mid  
            else:  
                l = mid+1 # 타겟에 도달 못했으면 그 다음부터 다시 탐색  
        answer.append(len(pool)-l)   
    - bisect 라는 이진탐색모듈도 있음
        - bisect_left(a, x)  : 정렬된 a에 x를 삽입할 위치를 리턴한다. x가 이미 있는 경우는 x의 위치를 반환한다.
        - bisect_right(a, x) : 정렬된 a에 x를 삽입할 위치를 리턴한다. x가 이미 있는 경우는 오른쪽(뒤)의 인덱스를 리턴한다.
        - answer.append(len(pool) - bisect_left(pool, find)) 와 결과가 같다.
