from ..utils.common_utils import run_command
from device_manager import get_adb_devices
from ..utils.logger import DDLogger
import time


class DeviceHandler:

    REBOOT_WAIT_TIME = 90

    def reset_device(self):
        raise NotImplementedError("Reset Device not Implemented.")

    def restart_device(self):
        """

        :return:
        """
        restart_device_args = ['adb', '-s', self.target_device_id, 'reboot']
        run_command(restart_device_args)
        time.sleep(DeviceHandler.REBOOT_WAIT_TIME)
        if self.target_device_id not in get_adb_devices():
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
        raise NotImplementedError("Gets UIAutomator handle for the current device")

    def __str__(self):
        return self.get_name()

