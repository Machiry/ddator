__author__ = 'machiry'
import os
import subprocess
import xml.dom.minidom
import random
import string


def create_dirs(dir_path):
    """
    Create the provided directory path only it it does not exist.
    :param dir_path: Path of the directory to be created.
    :return: None
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def read_file_lines(curr_file):
    """
    Read the contents of the provided file line by line.
    :param curr_file: full path of the file to read.
    :return: List containing lines of the file.
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


def get_random_text(length=0):
    """
    Get random text of specified length.
    :param length: Length of the random text.
    :return:  Randomly generated text.
    """
    if length <= 0:
        length = random.randint(1, 16)
    to_ret = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    return to_ret


def run_command(args, cmd_input=None):
    """
    Run the provided program.
    :param args: program to run and corresponding arguments.
    :param cmd_input: standard input for the program.
    :return: tuple containing (ret_code, output_line, err_lines)
    """
    output_lines = []
    err_lines = []
    ret_code = -255
    if args:
        cmd_line = " ".join(args)
        p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout_data, stderr_data) = p.communicate(input=cmd_input)
        # Remove empty lines
        output_lines = filter(lambda x: x, map(lambda x: x.strip(), stdout_data.split('\n')))
        # Remove empty lines
        err_lines = filter(lambda x: x, map(lambda x: x.strip(), stderr_data.split('\n')))
        ret_code = p.wait()

    return ret_code, output_lines, err_lines


def _get_all_leafs(curr_element):
    if len(curr_element.childNodes) == 0:
        return [curr_element]
    to_ret = []
    for curr_child in curr_element.childNodes:
        to_ret.extend(_get_all_leafs(curr_child))
    return to_ret


def get_all_leaf_elements(xml_text):
    """
    Get all leaf elements from the provided XML text.
    :param xml_text: XML text to be parsed.
    :return: list containing all leaf elements of the XML
    """
    root_element = xml.dom.minidom.parseString(xml_text)
    return _get_all_leafs(root_element)

