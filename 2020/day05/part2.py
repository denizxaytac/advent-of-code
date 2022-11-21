import math

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    highest_seat_id = float('-inf')
    lowest_seat_id = float('inf')
    all_seat_ids = list()
    for line in content:
        row = [0, 127]
        for char in line[:7]:
            half = (row[1] - row[0]) // 2
            if char == "F":
                row = [row[0], row[0] + half]
            elif char == "B":
                row = [row[0] + half + 1, row[1]]
        col = [0, 7]
        for char in line[7:]:
            half = (col[1] - col[0]) // 2
            if char == "L":
                col = [col[0], col[0] + half]
            elif char == "R":
                col = [col[0] + half + 1, col[1]]        
        seat_id = (row[0] * 8) + col[0]
        all_seat_ids.append(seat_id)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
        if seat_id < lowest_seat_id:
            lowest_seat_id = seat_id
    for num in range(lowest_seat_id, highest_seat_id + 1):
        if num not in all_seat_ids:
            return num

if __name__ == "__main__":
    print(solution('input.txt')) 
