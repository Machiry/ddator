__author__ = 'machiry'
import os


def create_dirs(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def read_file_lines(curr_file):
    """

    :param curr_file:
    :return:
    """
    file_lines = []
    if os.path.exists(curr_file):
        fp = open(curr_file, "r")
        for curr_line in fp.readlines():
            curr_line = curr_line.strip()
            if curr_line:
                file_lines.append(curr_line)
        fp.close()
    return file_lines
