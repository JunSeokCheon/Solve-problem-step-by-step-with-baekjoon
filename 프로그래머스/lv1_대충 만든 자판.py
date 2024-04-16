def solution(keymap, targets):
    answer = []
    
    for word in targets:
        # 해당 단어를 완성하는 횟수 저장 변수
        time = 0
    
        for alpha in word:
            # 완성 여부 판단 flag
            flag = False
            # 최대 변환이 100이니깐 101로 첫 값 설정
            trans = 101
            
            for key in keymap:
                # targets의 문자가 keymap 안에 존재하면 trans 횟수 갱신
                if alpha in key:
                    trans = min(trans, key.index(alpha)+1)
                    flag = True
            
            # 없으면 변환 횟수 -1로 만들고 break
            if flag == False:
                time = -1
                break
            
            # 변환 횟수 저장
            time += trans
        
        # tragets 문자열 최종 횟수 저장
        answer.append(time)
                    
    return answer