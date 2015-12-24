import threading
from ..utils.logger import DDLogger
from devices_helper import get_adb_devices
from emulator_handler import EmulatorHandler
from real_device_handler import RealDeviceHandler

# Lock to manage devices
_devices_lock = threading.Lock()

# Structures that hold devices according to corresponding states
_available_devices = None
_free_devices = None
_busy_devices = None


def get_available_devices():
    """
    Get total number of available devices.
    :return: int: Number of available devices.
    """
    global _available_devices
    global _free_devices
    global _busy_devices
    ret_val = 0
    if _available_devices is None:
        with _devices_lock:
            _available_devices = []
            _free_devices = []
            _busy_devices = []
            for device_name in get_adb_devices():
                # if the device is emulator
                # TODO: better check?
                if device_name.startswith('emulator'):
                    dev_handler = EmulatorHandler(device_name)
                else:
                    # else, its a real device.
                    dev_handler = RealDeviceHandler(device_name)
                _available_devices.append(dev_handler)
                # initially all devices are free.
                _free_devices.append(dev_handler)
    ret_val = len(_available_devices)
    return ret_val


def get_free_device():
    """
    This method is used to get any free device to be used for testing.
    :return: DeviceHandler for any available free device else None.
    """
    global _devices_lock
    global _free_devices
    global _busy_devices

    to_ret = None
    with _devices_lock:
        # if there are any free devices.
        if len(_free_devices) != 0:
            # get the top device
            to_ret = _free_devices[0]
            _free_devices = _free_devices[1:]
            # Add the handler to to busy devices.
            _busy_devices.append(to_ret)
    return to_ret


def put_free_device(to_release):
    """
    This method is used to release a device.
    :param to_release: Device handler of the device to be released.
    :return: True/False depending on success or failure respectively.
    """
    global _devices_lock
    global _free_devices
    global _busy_devices

    to_ret = False
    if to_release is not None and (to_release not in _free_devices):
        with _devices_lock:
            if to_release in _busy_devices:
                # remove from busy devices.
                _busy_devices.remove(to_release)
                to_ret = True
            else:
                DDLogger.write_failure_message("Target Device:" + str(to_release) + " to release not in busy devices.")
            # add the device into free devices.
            _free_devices.append(to_release)
    return to_ret



