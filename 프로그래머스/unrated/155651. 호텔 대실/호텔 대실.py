def solution(book_time):
    answer = 1

    for time in book_time:
        time[0], time[1] = int(time[0][0:2]) * 60 + int(time[0][3:]), int(time[1][0:2]) * 60 + int(time[1][3:])

    book_time.sort(key = lambda x : x[0], reverse = False)

    start_time, end_time = book_time[0][0], book_time[0][1]

    reserve = []
    reserve.append([start_time, end_time])
    book_time.pop(0)

    for case in book_time:
        next_start, next_end = case[0], case[1]

        for num, room in enumerate(reserve):
            if next_start >= room[1] + 10:
                reserve[num] = [next_start, next_end]
                break
        else:
            answer += 1
            reserve.append([next_start, next_end])
    
    return answer