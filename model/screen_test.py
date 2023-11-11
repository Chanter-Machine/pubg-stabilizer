import os
import shutil
import unittest

import cv2

from model.Screen import shotCut


# Define a simple function to test
def add(x, y):
    return x + y

# Create a test case by subclassing unittest.TestCase
class TestAddFunction(unittest.TestCase):

    # Each test is a method whose name starts with 'test'
    def test_add_new_guns_tmp(self):
        directory = "../resource/add_guns/"
        if not os.path.exists(directory):
            print("no directory")
            return

        new_gun_name = "m249"

        screen = shotCut(1780, 125, 614, 520)
        cv2.imwrite("../resource/add_guns/screen.bmp", screen)
        screenWepon1 = screen[0:40, 45:125]
        cv2.imwrite("../resource/add_guns/{0}.bmp".format(new_gun_name), screenWepon1)

    def test_commit_new_guns(self):
        directory = "../resource/add_guns/"
        if not os.path.exists(directory):
            print("no directory")
            return

        new_gun_name = "m249"
        source_path = '../resource/add_guns/{0}.bmp'.format(new_gun_name)
        destination_path = '../resource/guns/{0}.bmp'.format(new_gun_name)

        # Copy the file
        shutil.copyfile(source_path, destination_path)

    def test_subtract_10_and_print(self):
        input_array = [40, 28, 29, 28, 42, 43, 42, 43, 48, 48, 46, 47, 52, 53, 52, 48, 47, 48, 37, 38, 37, 38, 37, 38, 37, 38, 37, 38, 38, 39]
        # 对数组中的每个元素减去10
        result_array = [x - 5 for x in input_array]

        # 打印数组
        print("[" + ", ".join(map(str, result_array)) + "]")




# Run the tests
if __name__ == '__main__':
    unittest.main()
