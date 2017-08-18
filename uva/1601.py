class Point:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c


def read_data():
    w, h, n = (int(x) for x in input().split())
    if w == h == n == 0:
        return None
    graph = []
    for i in range(h):
        graph.append(input()[:w])
    return graph


def get_connecting_graph(graph):
    h = len(graph)
    w = len(graph[0])
    start = Point()
    end = Point()
    order = 1
    number = [[-1] * w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] != '#':
                number[i][j] = order
                order += 1
            if graph[i][j] == 'a':
                start.a = number[i][j]
            if graph[i][j] == 'b':
                start.b = number[i][j]
            if graph[i][j] == 'c':
                start.c = number[i][j]
            if graph[i][j] == 'A':
                end.a = number[i][j]
            if graph[i][j] == 'B':
                end.b = number[i][j]
            if graph[i][j] == 'C':
                end.c = number[i][j]

    connecting_graph = [[] for i in range(order + 1)]
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
    connecting_graph[0].append(0)
    return connecting_graph, start, end


def BFS(connecting_graph, start, end):
    import collections
    q = collections.deque()
    n = len(connecting_graph)
    visited = [[[False] * n for j in range(n)] for i in range(n)]
    visited[start.a][start.b][start.c] = True
    q.append((0, start))
    while not len(q) == 0:
        step, p = q.popleft()
        if (p.a, p.b, p.c) == (end.a, end.b, end.c):
            return step
        for i in connecting_graph[p.a]:
            for j in connecting_graph[p.b]:
                for k in connecting_graph[p.c]:
                    if not visited[i][j][k]:
                        if j and i == j or k and i == k or k and j == k:
                            # No more than one ghost occupies one position at the end of the step
                            continue
                        if j and i == p.b and j == p.a or k and i == p.c and k == p.a or k and j == p.c and k == p.b:
                            # No pair of ghosts exchange their positions one another in the step.
                            continue
                        # print(i, j, k, step + 1)
                        visited[i][j][k] = True
                        q.append((step + 1, Point(i, j, k)))
    return None


def main():
    while True:
        graph = read_data()
        if graph is None:
            break
        connecting_graph, start, end = get_connecting_graph(graph)
        print(BFS(connecting_graph, start, end))


if __name__ == '__main__':
    main()
