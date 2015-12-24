__author__ = 'machiry'
import os
from ..utils.common_utils import run_command
from ..utils.logger import DDLogger

"""
Module containing all helper functions to deal with APK
"""


def decompress_apk(apk_fp, dst_folder):
    """
    Decompress the provided APK
    :param apk_fp: absolute path of the apk to decompress.
    :param dst_folder: folder in which the apk need to be decompress.
    :return: true/false => success/failure.
    """
    apk_tool_path = os.environ['APK_TOOL_PATH']
    apk_tool_args = ['java', '-jar', apk_tool_path, 'd', '-f', '-o', dst_folder, apk_fp]
    ret_code, _, _ = run_command(apk_tool_args)
    if ret_code != 0:
        DDLogger.write_failure_message("APK Tool failed to decompress APK. Will Try again by removing apktool cache.")
        remove_apk_tool_cache = ['rm', '-rf', '~/apktool/']
        run_command(remove_apk_tool_cache)

        ret_code, out_text, err_text = run_command(apk_tool_args)
        if ret_code != 0:
            DDLogger.write_failure_message("Failed to Decompress APK (using apk_tool):" + str(apk_fp) +
                                           "\n Failed With:" + out_text + "\n Error Text:" + err_text)
    return ret_code == 0 and os.path.exists(os.path.join(dst_folder, "AndroidManifest.xml"))
