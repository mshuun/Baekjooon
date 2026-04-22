import sys
sys.setrecursionlimit(1 << 25)


def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

    # 값 압축 (좌표 압축)
    values = sorted(set(a))
    value_to_rank = {v: i + 1 for i, v in enumerate(values)}
    rank_to_value = [0] + values  # 인덱스가 1부터 시작하도록

    # 배열 값을 랭크로 변환
    a = [value_to_rank[x] for x in a]

    u = len(values)  # 고유한 값의 수

    # 영속 세그먼트 트리 노드 클래스
    class Node:
        __slots__ = ('left', 'right', 'count')

        def __init__(self, left=None, right=None, count=0):
            self.left = left
            self.right = right
            self.count = count

    # 트리 업데이트 함수
    def update(prev, l, r, pos):
        if l == r:
            return Node(count=(prev.count if prev else 0) + 1)
        mid = (l + r) // 2
        if pos <= mid:
            left = update(prev.left if prev else None, l, mid, pos)
            right = prev.right if prev else None
        else:
            left = prev.left if prev else None
            right = update(prev.right if prev else None, mid + 1, r, pos)
        return Node(left, right, (left.count if left else 0) + (right.count if right else 0))

    # 쿼리 처리 함수
    def query(u_node, v_node, l, r, k):
        if l == r:
            return l
        mid = (l + r) // 2
        left_count = (u_node.left.count if u_node.left else 0) - \
            (v_node.left.count if v_node.left else 0)
        if left_count >= k:
            return query(u_node.left if u_node.left else Node(), v_node.left if v_node.left else Node(), l, mid, k)
        else:
            return query(u_node.right if u_node.right else Node(), v_node.right if v_node.right else Node(), mid + 1, r, k - left_count)

    # 각 인덱스까지의 트리 루트 저장
    roots = [None] * (n + 1)
    roots[0] = Node()

    for i in range(1, n + 1):
        roots[i] = update(roots[i - 1], 1, u, a[i - 1])

    # 쿼리 처리 및 결과 출력
    for i, j, k in queries:
        node_i_minus_1 = roots[i - 1]
        node_j = roots[j]
        res_rank = query(node_j, node_i_minus_1, 1, u, k)
        print(rank_to_value[res_rank])


if __name__ == '__main__':
    main()
