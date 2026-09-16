def solution(video_len, pos, op_start, op_end, commands):
    video_len = hm(video_len)
    pos = hm(pos)
    op_start = hm(op_start)
    op_end = hm(op_end)
    for cmd in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if cmd == "prev":
            pos = max(0,pos-10)
        else:
            pos = min(video_len,pos + 10)
        if op_start <= pos <= op_end:
            pos = op_end
            
    
    return f"{pos//60:02d}:{pos%60:02d}"


def hm(s):
    h,m = s.split(":")
    return int(h)*60 + int(m)