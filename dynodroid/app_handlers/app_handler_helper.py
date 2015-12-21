import os
from .apk_handler import ApkHandler
from .app_src_handler import AppSrcHandler


def get_app_handler(target_path, work_dir):
    """
    This method instantiates corresponding app handlers based on the provided file path.
    To add new app handler, this function needs to be modified.
    :param target_path: Path of the app that needs to be handled.
    :param work_dir: working directory (or log directory) to be used by corresponding hanlder.
    :return: Handler object or None
    """
    to_ret = None
    if os.path.isfile(target_path) and target_path.lower().endswith('.apk'):
        to_ret = ApkHandler(target_path, work_dir)
    elif os.path.isdir(target_path):
        to_ret = AppSrcHandler(target_path, work_dir)
    return to_ret
