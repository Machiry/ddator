from ..utils.common_utils import run_command
from devices_helper import get_adb_devices
from ..utils.logger import DDLogger
import time


class DeviceHandler(object):
    """
    This is an abstract class that represents a device, used to perform all functions on the device.
    Any device handler should inherit this and implement corresponding methods.
    """

    # Number of seconds to wait for the device to reboot.
    REBOOT_WAIT_TIME = 90

    def reset_device(self):
        """
        Reset the device
        :return: True/False => Success/Failure
        """
        raise NotImplementedError("Reset Device not Implemented.")

    def restart_device(self):
        """
        Restart the device.
        :return: True/False => Success/Failure
        """
        # restart device
        restart_device_args = ['adb', '-s', self.target_device_id, 'reboot']
        run_command(restart_device_args)
        # wait for some time.
        time.sleep(DeviceHandler.REBOOT_WAIT_TIME)
        if self.target_device_id not in get_adb_devices():
            # if the device is no, up. wait for more time.
            time.sleep(DeviceHandler.REBOOT_WAIT_TIME / 2)
        if self.target_device_id not in get_adb_devices():
            DDLogger.write_failure_message("Device:" + str(self.target_device_id) + " failed to Reboot.")
            return False
        return True

    def run_command(self, args):
        raise NotImplementedError("Run Command not Implemented.")

    def get_name(self):
        return "InvalidDevice"

    def get_ui_handle(self):
        """
        This method gets the UIAutomator handle for the current device
        :return: UI Automator handle for this device.
        """
        raise NotImplementedError("get_ui_handle not implemented.")

    def __str__(self):
        return self.get_name()

