__author__ = 'machiry'
import os


def create_dirs(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
