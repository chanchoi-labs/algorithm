# https://school.programmers.co.kr/learn/courses/30/lessons/12978
# 다익스트라

class Mael():

    def __init__(self, N, road, K):

        self.N = N # 마을 수 (노드수)
        self.road = road # 간선정보 (연결, 가중치)
        self.K = K # 시감

        self.graph = dict() # 연결리스트
        for i in range(N+1):
            self.graph[i] = []
            for r in self.road:
                if r[0]==i:
                    self.graph[i].append((r[1],r[2]))
                if r[1]==i:
                    self.graph[i].append((r[0],r[2]))

        print(self.graph)
                        
            


def solution(N, road, K):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer

# main
if __name__ == "__main__":
    m = Mael(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)

