from utils import utils
import cv2 as cv
import numpy as np
from PIL import Image

def part1(input_img: Image) -> int:
    print('-----Part1-----')
    ans: int = 0
    # for each char apply mask to get binary image
    # depth first search to separate segments
    # when none append all pos to array

    img = cv.imread('input_img.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 9 chars, x 31
    # 0 31 62 93 124 ...
    ret, thresh = cv.threshold(gray, 0, 31, cv.THRESH_BINARY_INV)
    cv.imwrite('input_img.png', thresh)
    #
    # # noise removal
    # kernel = np.ones((1, 1), np.uint8)
    # opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
    #
    # # sure background area
    # sure_bg = cv.dilate(opening, kernel, iterations=3)
    #
    # # Finding sure foreground area
    # dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
    # ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    #
    # # Finding unknown region
    # sure_fg = np.uint8(sure_fg)
    # unknown = cv.subtract(sure_bg, sure_fg)
    #
    # # Marker labelling
    # ret, markers = cv.connectedComponents(sure_fg)
    #
    # # Add one to all labels so that sure background is not 0, but 1
    # markers = markers + 1
    #
    # # Now, mark the region of unknown with zero
    # markers[unknown == 255] = 0
    # markers = cv.watershed(img, markers)
    # img[markers == -1] = [255, 0, 0]
    # print(markers)

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
    print(pixel_arr)
    input_img = Image.fromarray(pixel_arr)
    input_img.save('input_img.png')
    return input_img

def main() -> None:
    print('-----DayN-----')
    input_str: str = utils.read_str('test.txt')
    input_arr: list[list[str]] = utils.read_char_arr('test.txt')
    distinct_chars = get_distinct_chars(input_str)
    input_img = convert_input_to_img(input_arr, distinct_chars)
    print(part1(input_img))
    # print(part2(input_data))

if __name__ == '__main__':
    main()