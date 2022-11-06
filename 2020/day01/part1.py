
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    content = [int(num) for num in content]
    for p1 in range(len(content) - 1):
        for p2 in range(p1 + 1, len(content)):
            if content[p1] + content[p2] == 2020:
                return content[p1] * content[p2]

if __name__ == "__main__":
    print(solution('input.txt')) 
