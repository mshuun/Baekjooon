def is_possible_to_visit_cells(R, C, K):
    # Always possible when K = 1
    if K == 1:
        return 1

    # For K > 1, check if the total number of cells is even
    total_cells = R * C
    if total_cells % 2 == 0:
        return 1
    else:
        return 0
R,C,K = map(int,input().split())
print(is_possible_to_visit_cells(R,C,K))