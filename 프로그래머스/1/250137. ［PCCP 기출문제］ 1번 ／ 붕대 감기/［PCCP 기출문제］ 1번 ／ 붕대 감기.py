def solution(bdg, max_hp, atks):
    hp, prev = max_hp, 0
    t, heal, bonus = bdg

    for time, dmg in atks:
        gap = time - prev - 1
        new_hp = hp + gap * heal + (gap // t) * bonus
        hp = min(max_hp, new_hp) - dmg

        if hp <= 0:
            return -1

        prev = time

    return hp