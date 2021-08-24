def solution(s):
    answer = ''
    cursor = 0
    tmp = ''
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while cursor < len(s):
        if s[cursor] in number:
            answer += s[cursor]
            cursor += 1
            continue
        tmp += s[cursor]
        if tmp in word:
            answer += str(word.index(tmp))
            tmp = ''
        cursor += 1
    return int(answer)
