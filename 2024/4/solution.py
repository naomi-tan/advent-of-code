from utils.utils import *

def part1(input_data: list[list[str]]) -> int:
    print('-----Part1-----')
    ans = 0
    row = 0
    # search for all X
    for line in input_data:
        col = 0
        for char in line:
            if char == 'X':
                # get neighbours
                neighbours = get_neighbours(input_data, row, col, 1)
                i = 0
                for n in neighbours:
                    if n == 'M':
                        # if M get direction
                        dx = [-1, 0, 1, -1, 1, -1, 0, 1]
                        dy = [-1, -1, -1, 0, 0, 1, 1, 1]
                        x_pos: list[int] = [row, col]
                        m_pos: list[int] = [row + dy[i], col + dx[i]]
                        a_pos: list[int] = [row + 2*dy[i], col + 2*dx[i]]
                        s_pos: list[int] = [row + 3*dy[i], col + 3*dx[i]]
                        # check for A S in same direction
                        if (s_pos[0] >= 0) and (s_pos[0] < len(input_data[0])) and (s_pos[1] >= 0) and (s_pos[1] < len(input_data)):
                            if input_data[a_pos[0]][a_pos[1]] == 'A' and input_data[s_pos[0]][s_pos[1]] == 'S':
                                ans += 1
                    i += 1
            col += 1
        row += 1
    return ans

def part2(input_data: list[list[str]]) -> int:
    print('-----Part2-----')
    ans = 0
    row = 0
    # search for all A
    for line in input_data:
        col = 0
        for char in line:
            if char == 'A':
                # get neighbours
                neighbours = get_neighbours(input_data, row, col, 1)
                n_str = ''.join(neighbours)
                patterns = [r'M.M..S.S', r'S.M..S.M', r'S.S..M.M', r'M.S..M.S']
                for p in patterns:
                    if len(re.findall(p, n_str)) > 0:
                        ans += 1
                        break
                # check match
            col += 1
        row += 1
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data = read_char_arr('input.txt')
    print(part1(input_data))
    print(part2(input_data))
    # 2010 too high

if __name__ == '__main__':
    main()