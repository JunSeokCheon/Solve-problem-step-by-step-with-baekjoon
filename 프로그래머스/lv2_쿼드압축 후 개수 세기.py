def solution(arr):
    answer = [0, 0]
    init = len(arr)
    
    def quad(a,b,l):
        start = arr[a][b]
        for i in range(a, a+l):
            for j in range(b, b+l):
                if start != arr[i][j]:
                    l = l//2
                    quad(a,b,l)
                    quad(a+l,b,l)
                    quad(a,b+l,l)
                    quad(a+l,b+l,l)
                    return
        
        answer[start] += 1
        
    quad(0,0,init)
    
    return answer