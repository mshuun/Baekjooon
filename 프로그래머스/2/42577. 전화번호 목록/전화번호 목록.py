def solution(phone_book):
    book = {v: i for i, v in enumerate(phone_book)}
    for p in phone_book:
        for i in range(len(p)):
            if p[:i] in book:
                return False
    return True