import threading
from ..utils.logger import DDLogger
from ..utils.common_utils import run_command
from emulator_handler import EmulatorHandler
from real_device_handler import RealDeviceHandler

# Lock to manage devices
_devices_lock = threading.Lock()

# Structures that hold devices according to corresponding states
_available_devices = None
_free_devices = None
_busy_devices = None


def get_adb_devices():
    """

    :return:
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


def get_available_devices():
    """

    :return:
    """
    global _available_devices
    global _free_devices
    global _busy_devices
    ret_val = 0
    if _available_devices is None:
        with _devices_lock:
            _available_devices = {}
            _free_devices = {}
            _busy_devices = {}
            for device_name in get_adb_devices():
                if device_name.startswith('emulator'):
                    dev_handler = EmulatorHandler(device_name)
                else:
                    dev_handler = RealDeviceHandler(device_name)
                _available_devices.append(dev_handler)
                _free_devices.append(dev_handler)
    ret_val = len(_available_devices)
    return ret_val


def get_free_device():
    """

    :return:
    """
    global _devices_lock
    global _free_devices
    global _busy_devices

    to_ret = None
    with _devices_lock:
        if len(_free_devices) != 0:
            to_ret = _free_devices[0]
            _free_devices = _free_devices[1:]
            _busy_devices.append(to_ret)
    return to_ret


def put_free_device(to_release):
    """

    :param to_release:
    :return:
    """
    global _devices_lock
    global _free_devices
    global _busy_devices

    to_ret = False
    if to_release is not None and (to_release not in _free_devices):
        with _devices_lock:
            if to_release in _busy_devices:
                _busy_devices.remove(to_release)
                to_ret = True
            else:
                DDLogger.write_failure_message("Target Device:" + str(to_release) + " to release not in busy devices.")
            _free_devices.append(to_release)
    return to_ret



