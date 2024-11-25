from itertools import combinations

def solve():
    N = int(input())
    S = [list(map(int, input().split())) for i in range(N)]

    players = range(N)
    min_diff = float('inf')

    # 팀1 조합만 생성
    for team1 in combinations(players, N // 2):
        team2 = [p for p in players if p not in team1]

        # 팀 점수 계산
        score1 = sum(S[i][j] for i in team1 for j in team1)
        score2 = sum(S[i][j] for i in team2 for j in team2)

        # 최소 차이 갱신
        min_diff = min(min_diff, abs(score1 - score2))

    print(min_diff)

solve()