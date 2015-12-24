from ..utils.logger import DDLogger
from ..utils.common_utils import run_command


def get_adb_devices():
    """
    This helper method returns all the devices detected by adb.
    :return: List of device ids provided by adb.
    """
    to_ret = []
    get_device_args = ['adb', 'devices']
    (ret_code, output_lines, err_lines) = run_command(get_device_args)
    if ret_code != 0:
        DDLogger.write_failure_message("Running adb devices failed with return code:" + str(ret_code))
    dev_start = False
    for curr_line in output_lines:
        if dev_start:
            dev_info = filter(lambda x: x.strip(), curr_line.split())
            device_name = dev_info[0]
            to_ret.append(device_name)
        else:
            dev_start = curr_line.startswith('List of devices attached')

    return to_ret
