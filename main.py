class Node:
    def __init__(self, x, y, pre):
        self.pre = pre
        self.x = x
        self.y = y
        self.next = []

    def compare(self, n):
        return self.x == n.x and self.y == n.y


tree = []


def main():
    x_array = y_array = [1, 2, 3, 4, 5, 6, 7, 8]
    for x in x_array:
        for y in y_array:
            n = Node(x, y, None)
            tree.append(n)
            print('Building ' + str(x) + str(y))
            horse(n)

    for t in tree:
        print_it(t, '')


def horse(n):
    filler = []
    if n.x + 2 <= 8 and n.y + 1 <= 8:
        filler.append(Node(n.x + 2, n.y + 1, n))
    if n.x + 2 <= 8 and n.y - 1 >= 1:
        filler.append(Node(n.x + 2, n.y - 1, n))
    if n.x - 2 >= 1 and n.y + 1 <= 8:
        filler.append(Node(n.x - 2, n.y + 1, n))
    if n.x - 2 >= 1 and n.y - 1 >= 1:
        filler.append(Node(n.x - 2, n.y - 1, n))
    if n.y + 2 <= 8 and n.x + 1 <= 8:
        filler.append(Node(n.x + 1, n.y + 2, n))
    if n.y + 2 <= 8 and n.x - 1 >= 1:
        filler.append(Node(n.x - 1, n.y + 2, n))
    if n.y - 2 >= 1 and n.x + 1 <= 8:
        filler.append(Node(n.x + 1, n.y - 2, n))
    if n.y - 2 >= 1 and n.x - 1 >= 1:
        filler.append(Node(n.x - 1, n.y - 2, n))

    n.next = trim(n, filler)

    for nx in n.next:
        horse(nx)


def trim(n, l):
    for x in l:
        if n.compare(x):
            l.remove(x)
    if n.pre is not None:
        trim(n.pre, l)
    return l


def print_it(tr, s):
    aux = s + str(tr.x) + str(tr.y) + '-'
    if len(tr.next) > 0:
        for t in tr.next:
            print_it(t, aux)
    else:
        sta = aux[:-1]
        stb = sta.split('-')
        if len(stb) == 64:
            print(sta)
        else:
            print(str(len(stb)) + ' -- ' + sta)


if __name__ == "__main__":
    main()
