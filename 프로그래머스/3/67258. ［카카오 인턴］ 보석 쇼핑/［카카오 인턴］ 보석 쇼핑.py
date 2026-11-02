def solution(gems):
    gems_num = len(set(gems))
    left_idx = 0
    right_idx = 1
    shortest_len = -1
    shortest_left_idx = -1
    shortest_right_idx = -1

    new_gems = {}
    new_gems[gems[0]] = 1
    while True:
        new_gems_num = len(new_gems)

        if new_gems_num == gems_num:
            new_len = right_idx - left_idx
            if shortest_len == -1 or new_len < shortest_len:
                shortest_left_idx = left_idx
                shortest_right_idx = right_idx
                shortest_len = right_idx - left_idx

            new_gems[gems[left_idx]] -= 1
            if new_gems[gems[left_idx]] == 0:
                new_gems.pop(gems[left_idx])
            left_idx += 1
        else:
            if right_idx == len(gems):
                break
            new_gems[gems[right_idx]] = new_gems.get(gems[right_idx],0) + 1
            right_idx += 1
            if right_idx > len(gems):
                break

    return [shortest_left_idx + 1, shortest_right_idx]
