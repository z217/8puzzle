from astar.Node import Node

direction: tuple = ((0, 1), (0, -1), (1, 0), (-1, 0))
open: list[Node] = []  # 待搜索状态
close: set = set()  # 已搜索状态
path: list[Node] = []  # 路径
solution: list[int] = []  # 解法，记录空格与数字的交换


# AStar算法
def AStar(start: list[list[int]], end: list[list[int]]) -> int:
    # 无解
    if not checkValid(start, end):
        return -1
    n = len(start)
    open.clear()
    close.clear()
    path.clear()
    solution.clear()
    endMap = {}
    for i in range(n):
        for j in range(n):
            endMap[end[i][j]] = (i, j)
    ID = 0
    open.append(Node(start, 0, 0, H(start, end, endMap), ID, ID))
    open[0].f = open[0].h
    ID += 1
    while len(open) > 0:
        open.sort(key=lambda s: s.f)
        cur = open.pop(0)
        path.append(cur)
        close.add(hashCode(cur.stat))

        # 是否完成
        if success(cur.stat, end, endMap):
            return cur.g

        # 查找空格位置
        cx, cy = -1, -1  # 空格
        for i in range(n):
            for j in range(n):
                if cur.stat[i][j] == 0:
                    cx = i
                    cy = j
                    break

        # 移动
        for k in range(4):
            nx, ny = cx + direction[k][0], cy + direction[k][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 生成新状态
            new = Node(cur.stat, 0, cur.g + 1, 0, ID, cur.cID)
            new.stat[cx][cy], new.stat[nx][ny] = new.stat[nx][ny], new.stat[cx][cy]
            ID += 1
            new.h = H(new.stat, end, endMap)
            new.f = F(new)
            # 表中没有该状态
            if hashCode(new.stat) not in close:
                index = -1
                for i in range(len(open)):
                    if success(new.stat, open[i].stat, endMap):
                        index = i
                        break
                # 找到该状态
                if index != -1:
                    if open[index].f > new.f:
                        open.pop(index)
                        open.append(new)
                # 没有找到该状态
                else:
                    open.append(new)
    # 无解
    return -1


# 后序递归寻找路径
def outpath(pID: int, s: int, step: int):
    if step < 0:
        return
    # 初始状态
    elif step == 0:
        print("Step(" + str(step) + ") ==> ")
        output(path[s].stat)  # 输出状态
        return
    # 前向查找父状态
    for i in range(s, -1, -1):
        if path[i].cID == pID:
            outpath(path[i].pID, i, step - 1)
    print("Step(" + str(step) + ") ==> ")
    output(path[s].stat)


def outExchangPath(pID: int, s: int, step: int, cx: int, cy: int) -> [int, int]:
    if step <= 0:
        return cx, cy
    for i in range(s, -1, -1):
        if path[i].cID == pID:
            (x, y) = outExchangPath(path[i].pID, i, step - 1, cx, cy)
            solution.append(path[s].stat[x][y])
            for j in range(len(path[s].stat)):
                for k in range(len(path[s].stat)):
                    if path[s].stat[j][k] == 0:
                        return j, k


# 评估函数
def H(cur: list[list[int]], end: list[list[int]], endMap: map) -> int:
    h = 0
    for i in range(len(cur)):
        for j in range(len(cur)):
            if cur[i][j] != end[i][j]:
                h += abs(i - endMap[cur[i][j]][0]) + abs(j - endMap[cur[i][j]][1])
    return h


# 评估函数
def F(node: Node) -> int:
    return node.g + node.h


# 是否完成
def success(cur: list[list[int]], end: list[list[int]], endMap: map) -> bool:
    return H(cur, end, endMap) == 0


# 求状态对应的哈希
def hashCode(stat: list[list[int]]) -> int:
    h = 0
    for i in stat:
        for j in i:
            h = h * 10 + j
    return h


# 是否有解
def checkValid(cur: list[list[int]], end: list[list[int]]) -> bool:
    s, e, n = 0, 0, len(cur)
    for i in range(n * n):
        for j in range(i):
            if cur[int(j / n)][j % n] != 0 and cur[int(j / n)][j % n] < cur[int(i / n)][i % n]:
                s += 1
            if end[int(j / n)][j % n] != 0 and end[int(j / n)][j % n] < end[int(i / n)][i % n]:
                e += 1
    return s & 1 == e & 1


# 输出函数
def output(stat: list[list[int]]):
    for i in stat:
        for j in i:
            print(j, end=' ')

        print()
