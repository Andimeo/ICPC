# bidirectional BFS


class Point:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c


def read_data():
    w, h, n = (int(x) for x in input().split())
    if w == h == n == 0:
        return None, None
    graph = []
    for i in range(h):
        graph.append(input()[:w])
    return graph, n


def get_connecting_graph(graph, n):
    h = len(graph)
    w = len(graph[0])
    start = Point()
    end = Point()
    order = 0
    number = [[-1] * w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] != '#':
                number[i][j] = order
                order += 1
            if graph[i][j].islower():
                start.__dict__[graph[i][j]] = number[i][j]
            if graph[i][j].isupper():
                end.__dict__[chr(ord(graph[i][j]) - ord('A') + ord('a'))] = number[i][j]
    if n <= 2:
        start.c = order
        end.c = order
        order += 1
    if n <= 1:
        start.b = order
        end.b = order
        order += 1
    connecting_graph = [[] for i in range(order)]
    if n <= 2:
        connecting_graph[order - 1].append(order - 1)
    if n <= 1:
        connecting_graph[order - 2].append(order - 2)
    xs = [0, -1, 0, 1, 0]
    ys = [0, 0, -1, 0, 1]
    for i in range(h):
        for j in range(w):
            if number[i][j] == -1:
                continue
            for k in range(5):
                nx = i + xs[k]
                ny = j + ys[k]
                if number[nx][ny] != -1:
                    connecting_graph[number[i][j]].append(number[nx][ny])
    return connecting_graph, start, end


def BFS(connecting_graph, start, end):
    import collections
    qf = collections.deque()
    qb = collections.deque()
    n = len(connecting_graph)
    dist = [[[-1] * n for j in range(n)] for i in range(n)]
    dist[start.a][start.b][start.c] = 0
    bdist = [[[-1] * n for j in range(n)] for i in range(n)]
    bdist[end.a][end.b][end.c] = 0
    qf.append(start)
    qb.append(end)
    while len(qf) != 0 or len(qb) != 0:
        # We have to traverse the search tree level by level
        fnum = len(qf)
        bnum = len(qb)
        while fnum > 0:
            fnum -= 1
            p = qf.popleft()
            if bdist[p.a][p.b][p.c] != -1:
                return dist[p.a][p.b][p.c] + bdist[p.a][p.b][p.c]
            for i in connecting_graph[p.a]:
                for j in connecting_graph[p.b]:
                    for k in connecting_graph[p.c]:
                        if dist[i][j][k] == -1:
                            if i == j or i == k or j == k:
                                # No more than one ghost occupies one position at the end of the step
                                continue
                            if i == p.b and j == p.a or i == p.c and k == p.a or j == p.c and k == p.b:
                                # No pair of ghosts exchange their positions one another in the step.
                                continue
                            # print(i, j, k, step + 1)
                            dist[i][j][k] = dist[p.a][p.b][p.c] + 1
                            qf.append(Point(i, j, k))
        while bnum > 0:
            bnum -= 1
            p = qb.popleft()
            if dist[p.a][p.b][p.c] != -1:
                return dist[p.a][p.b][p.c] + bdist[p.a][p.b][p.c]
            for i in connecting_graph[p.a]:
                for j in connecting_graph[p.b]:
                    for k in connecting_graph[p.c]:
                        if bdist[i][j][k] == -1:
                            if i == j or i == k or j == k:
                                # No more than one ghost occupies one position at the end of the step
                                continue
                            if i == p.b and j == p.a or i == p.c and k == p.a or j == p.c and k == p.b:
                                # No pair of ghosts exchange their positions one another in the step.
                                continue
                            # print(i, j, k, step + 1)
                            bdist[i][j][k] = bdist[p.a][p.b][p.c] + 1
                            qb.append(Point(i, j, k))
    return None


def main():
    while True:
        graph, n = read_data()
        if graph is None:
            break
        connecting_graph, start, end = get_connecting_graph(graph, n)
        print(BFS(connecting_graph, start, end))


if __name__ == '__main__':
    main()
