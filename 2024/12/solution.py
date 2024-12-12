from utils import utils
import cv2 as cv
import numpy as np
from PIL import Image
# import skimage
from skimage.measure import label, regionprops
import skimage.io as io

def part1(input_str, input_arr) -> int:
    print('-----Part1-----')
    ans: int = 0

    distinct_chars = get_distinct_chars(input_str)

    for i in range(len(input_arr)):
        for j in range(len(input_arr[0])):
            index = distinct_chars.index(input_arr[i][j])
            input_arr[i][j] = index

    for i in range(len(distinct_chars)):
        bin_img = np.asarray(list(map(lambda a: list(map(lambda b: int(b==i)*255, a)), input_arr)), dtype=np.uint8)
        input_img = Image.fromarray(bin_img)
        input_img.save('input_img.png')
        im = io.imread('input_img.png')
        regions = regionprops(im.astype(int))
        area = regions[0].num_pixels
        x = regions[0].perimeter
        print(x)
        # masked_arr = np.ma.masked_where(np_arr !=i, np_arr)
        # print(masked_arr)

    # for each char apply mask to get binary image
    # depth first search to separate segments
    # when none append all pos to array

    # https://cse.usf.edu/~r1k/MachineVisionBook/MachineVision.files/MachineVision_Chapter2.pdf
    # threshold filter each letter
    # clustering algorithm
    return ans

def part2(input_data: list[list[str]]) -> int:
    print('-----Part2-----')
    ans: int = 0
    return ans

def get_distinct_chars(input_data: str):
    return sorted(list(set(list(input_data.replace('\n','')))))

def convert_input_to_img(input_data, distinct_chars):
    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            index = distinct_chars.index(input_data[i][j])
            input_data[i][j] = index
    pixel_arr = np.array(input_data, dtype=np.uint8)
    pixel_arr = pixel_arr * int(255 / np.max(pixel_arr))
    input_img = Image.fromarray(pixel_arr)
    input_img.save('input_img.png')
    return input_img

def mask_arr(input_data, distinct_chars):
    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            index = distinct_chars.index(input_data[i][j])
            input_data[i][j] = index
    np_arr = np.asarray(input_data, dtype=np.uint8)
    masked_arr = np.ma.masked_where(np_arr != 2, np_arr)
    return masked_arr

def main() -> None:
    print('-----DayN-----')
    file = 'input.txt'
    input_str: str = utils.read_str(file)
    input_arr: list[list[str]] = utils.read_char_arr(file)
    print(part1(input_str, input_arr))
    # print(part2(input_data))

if __name__ == '__main__':
    main()