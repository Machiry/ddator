__author__ = 'machiry'
from ..utils.common_utils import run_command

class AppHandler:

    def get_name(self):
        return "InvalidAppHandler"

    def build_app(self):
        raise NotImplementedError("Build App not overridden.")

    def get_app_name(self):
        raise NotImplementedError("get app name Not implemented.")

    @staticmethod
    def install_apk(apk_name, target_device_handler):
        """

        :param apk_name:
        :param target_device_handler:
        :return:
        """
        target_args = ['adb', '-s', target_device_handler.target_device_id, 'install', apk_name]
        ret_code, _, _ = run_command(target_args)
        return ret_code == 0

    def install_app(self, device_handler):
        raise NotImplementedError("Install App not overridden")

    def __str__(self):
        return self.get_name()
