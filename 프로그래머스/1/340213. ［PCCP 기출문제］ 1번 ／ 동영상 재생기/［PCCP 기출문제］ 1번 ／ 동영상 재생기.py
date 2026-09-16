def solution(video_len, pos, op_start, op_end, commands):
    video_len, pos, op_start, op_end = map(a,(video_len,pos,op_start,op_end))
    if op_start <= pos <= op_end: 
        pos = op_end
            
    for cmd in commands:        
        pos = [min(video_len,pos+10),max(0,pos-10)][cmd=="prev"]
        if op_start<=pos<=op_end:
            pos = op_end
                
    return f"{pos//60:02d}:{pos%60:02d}"


def a(t):
    m, s = map(int, t.split(":"))
    return m*60+s