def read_data():
    n = int(input())
    if n == 0:
        return None
    return [int(item) for item in input().split()]


def is_sorted(l):
    for i in range(1, len(l)):
        if l[i] <= l[i - 1]:
            return False
    return True


def h(l):
    cnt = 0 if l[0] == 1 else 1
    for i in range(1, len(l)):
        if l[i - 1] + 1 != l[i]:
            cnt += 1
    return cnt


def DFS(d, maxd, book):
    if d * 3 + h(book) > maxd * 3:
        return False
    if is_sorted(book):
        return True
    n = len(book)
    old_book = book.copy()
    for i in range(n):
        for j in range(i, n):
            paste_board = book[:i] + book[j + 1:]
            for k in range(len(paste_board) + 1):
                book.clear()
                book.extend(paste_board[:k])
                book.extend(old_book[i:j + 1])
                book.extend(paste_board[k:])
                assert len(book) == len(old_book)
                if DFS(d + 1, maxd, book):
                    return True
                # restore the original array
                book.clear()
                book.extend(old_book)
    return False


def main():
    kcase = 1
    while True:
        l = read_data()
        if l is None:
            break
        for maxd in range(1, 9):
            if DFS(0, maxd, l):
                print('Case {}: {}'.format(kcase, maxd))
                kcase += 1
                break


if __name__ == '__main__':
    main()
