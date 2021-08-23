- 시간초과 때문에 dict에 다 넣고 이진검색으로 찾아야 함
- itertools 보다 for문 돌면서 dict 넣는게 편함
- 이진탐색
    - 정렬된 배열에서 탐색 범위를 절반씩 좁혀가며 데이터 탐색 O(logN)
    -   l = 0  
        r = len(pool)  
        mid = 0  
        while l < r:  
            mid = (r+l)//2  
            if pool[mid] >= target:  
                r = mid  
            else:  
                l = mid+1  
        answer.append(len(pool)-l)   
