def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()  # 1단계
    
    for i in new_id:
        if i.isalnum() or i in ['-', '_', '.']:
            answer += i      # 2단계
            
    while '..' in answer:
        answer = answer.replace('..', '.')
                             # 3단계
            
    if answer[0] == '.':
        if len(answer) != 1:
            answer = answer[1:]
        else:
            answer = ''
    if answer and answer[-1] == '.':
        if len(answer) != 1:
            answer = answer[:-1] 
        else:
            answer = ''          # 4단계
    
    if answer == '':
        answer = 'a'             # 5단계
        
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1] # 6단계
            
    while len(answer) <= 2:
        answer += answer[-1]     # 7단계
        
    return answer
