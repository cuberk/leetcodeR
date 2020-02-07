'''
最初的思路，就是顺着题目的意思，把每分钟的情况都模拟出来
'''

def orangesRotting(grid):
    minute = 0
    M = len(grid)
    if M:
        N = len(grid[0])
    while True:
        flagOne = False     # 假设当前没有新鲜橘子
        flagThree = False   # 假设当前没有要腐烂的新鲜橘子
        for i in range(M):
            for j in range(N):  # 第一次遍历，将上次标记要腐烂的橘子设为腐烂
                if grid[i][j] == 3:
                    grid[i][j] = 2
        for i in range(M):
            for j in range(N):  # 遍历
                if grid[i][j] == 1:
                    flagOne = True  # 还有新鲜橘子
                if grid[i][j] == 2: # 腐烂橘子
                    ifriend, jfriend = [], []
                    if i > 0:
                        ifriend.append(i - 1)
                    if i < M - 1:
                        ifriend.append(i + 1)
                    if j > 0:
                        jfriend.append(j - 1)
                    if j < N - 1:
                        jfriend.append(j + 1)
                    friends = []
                    for friendi in ifriend:
                        friends.append([friendi, j])
                    for friendj in jfriend:
                        friends.append([i, friendj])
                    for friend in friends:
                        tmp0, tmp1 = friend[0], friend[1]
                        if grid[tmp0][tmp1] == 1:
                            grid[tmp0][tmp1] = 3 # 下分钟腐烂的新鲜橘子
                            flagThree = True
        if flagThree:
            minute += 1
        else:
            if flagOne:
                return -1
            else:
                return minute

cases = [
    [[[2,1,1],[1,1,0],[0,1,1]],4],
    [[[2,1,1],[0,1,1],[1,0,1]],-1],
    [[[0,2]],0]
]
for case in cases:
    if orangesRotting(case[0]) == case[1]:
        print("case:" + str(case[0]) + '通过测试')

