

n, m = map(int, input().split())

card = list(map(int, (input().split())))

card_max = 0

# 3개의 숫자를 더해주기 위해 리스트범위를  n-3 +1 해준다.
for i in range(n - 3 + 1):
    result = card[i] # 맨 앞 첫번째 숫자 더해준다. (점점 오른쪽으로 갈 것임)
    for j in range(i+1, n):
        result += card[j] # i번째 다음의 숫자를 더해준다. (점점 오른쪽으로 갈 것임)
        for k in range(j+1, n):
            result += card[k] # j번째 다음의 숫자를 더해준다. ( 점점 오른쪽으로 갈 것임)

            if result <= m: # 그 세개를 더한 숫자가 m보다 작으면
                if result > card_max: # 그게 최댓값이면
                    card_max = result # 저장한다.

            result -= card[k] # 만약에 아니라면 오른쪽으로 갈것이기때문에 더해줬던것을 빼준다.
        result -= card[j] # 마찬가지로 k번째가 끝나면 다음 인덱스로 가서 더해줄것이기때문에 더해줬던것을 빼준다.
    result -= card[i] # 같은 방법

print(card_max)
