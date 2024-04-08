from datetime import datetime

# 입력 데이터 처리
N, M, P = map(int, input().split())
participants = list(input().split())
submissions = [list(input().split()) for _ in range(P)]

# 참가자 정보 초기화
scores = {participant: 0 for participant in participants}  # 참가자별 총 점수
attempts = {participant: {str(i): [] for i in range(1, N+1)}
            for participant in participants}  # 문제별 시도 기록

# 제출 기록 처리
for problem, time, name, result in submissions:
    # 시간 변환
    time = datetime.strptime(time, "%H:%M")
    # 제출 기록 추가
    attempts[name][problem].append((time, result))

# 점수 계산
for i in range(1, N+1):
    problem_scores = []
    for participant, problems in attempts.items():
        problem_attempts = problems[str(i)]
        if not problem_attempts:  # 제출 기록 없음
            scores[participant] += M + 1
            continue

        first_wrong_time = None
        solve_time = None
        for attempt_time, result in problem_attempts:
            if result == "wrong" and first_wrong_time is None:
                first_wrong_time = attempt_time
            elif result == "solve":
                solve_time = attempt_time
                break

        if solve_time:  # 문제 해결
            if first_wrong_time is None:  # 첫 시도에 해결
                scores[participant] += M + 1
            else:
                problem_scores.append(
                    (solve_time - first_wrong_time, participant))
        else:  # 해결 실패
            scores[participant] += M

    # 문제 점수 계산 및 부여
    problem_scores.sort()
    for rank, (_, participant) in enumerate(problem_scores, start=1):
        scores[participant] += rank

# 결과 정렬 및 출력
sorted_participants = sorted(scores.items(), key=lambda x: (x[1], x[0]))
sorted_names = [name for name, _ in sorted_participants]

print(*sorted_names)
