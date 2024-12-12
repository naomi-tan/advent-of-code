from utils import utils
import cv2 as cv
import numpy as np
from PIL import Image
from skimage.measure import regionprops
import skimage.io as io
import scipy.ndimage as sp
from skimage.feature import blob_log

def part1(input_str, input_arr) -> int:
    print('-----Part1-----')
    ans: int = 0

    distinct_chars = get_distinct_chars(input_str)
    # needs some sort of blob separation

    for i in range(len(input_arr)):
        for j in range(len(input_arr[0])):
            index = distinct_chars.index(input_arr[i][j])
            input_arr[i][j] = index

    for i in range(len(distinct_chars)):
        bin_img = np.asarray(list(map(lambda a: list(map(lambda b: int(b==i)*255, a)), input_arr)), dtype=np.uint8)

        input_img = Image.fromarray(bin_img)
        input_img.save('input_img.png')
        im = io.imread('input_img.png')
        im2 = sp.binary_fill_holes(im) * 255
        [p, a] = perimeter(im2)

        ans += p*a

    # for each char apply mask to get binary image
    # depth first search to separate segments
    # when none append all pos to array

    # https://cse.usf.edu/~r1k/MachineVisionBook/MachineVision.files/MachineVision_Chapter2.pdf
    # threshold filter each letter
    # clustering algorithm
    return ans

def perimeter(bin_arr):
    padded_arr = np.zeros((bin_arr.shape[0] + 2, bin_arr.shape[1] + 2))
    padded_arr[1:bin_arr.shape[0]+1, 1:bin_arr.shape[1]+1] = bin_arr
    [x_ls, y_ls] = np.where(padded_arr == 255)
    area = len(x_ls)
    perim = 0
    for x, y in zip(x_ls, y_ls):
        if padded_arr[x - 1 , y] == 0:
            perim += 1
        if padded_arr[x + 1 , y] == 0:
            perim += 1
        if padded_arr[x, y - 1] == 0:
            perim += 1
        if padded_arr[x, y + 1] == 0:
            perim += 1
    # print(perim) # 32 is 28, 30 is 22
    return [perim, area]

def part2(input_data: list[list[str]]) -> int:
    print('-----Part2-----')
    ans: int = 0
    return ans

def get_distinct_chars(input_data: str):
    return sorted(list(set(list(input_data.replace('\n','')))))

def main() -> None:
    print('-----DayN-----')
    file = 'test.txt'
    input_str: str = utils.read_str(file)
    input_arr: list[list[str]] = utils.read_char_arr(file)
    print(part1(input_str, input_arr))
    # print(part2(input_data))

if __name__ == '__main__':
    main()