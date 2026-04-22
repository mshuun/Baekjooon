while True:
    pw = input()
    if pw == 'end':
        break

    # 모음을 포함하는지 확인
    acc = any(char in 'aeiou' for char in pw)

    # 연속된 모음/자음, 중복된 문자 확인
    cc, vc = 0, 0
    last_char = 'A'
    bcc = True
    for char in pw:
        if char in 'aeiou':
            cc = 0
            vc += 1
        else:
            vc = 0
            cc += 1
        
        # 연속된 모음/자음, 중복된 문자 확인
        if char == last_char and char not in 'eo':
            bcc = False
        if cc == 3 or vc == 3:
            bcc = False
        if not bcc:
            break
        last_char = char

    if acc and bcc:
        print(f'<{pw}> is acceptable.')
    else:
        print(f'<{pw}> is not acceptable.')
