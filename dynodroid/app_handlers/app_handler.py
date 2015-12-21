__author__ = 'machiry'
from ..utils.common_utils import run_command


class AppHandler(object):
    """
    This class defines an interface for app handlers.
    Any new app handler should inherit from this
     -> define the corresponding abstract methods.
     -> add instantiation in app_handler_helper.py

    """

    def get_name(self):
        """
        Name of the class, used in str function.
        :return: String representing name of the class.
        """
        return "InvalidAppHandler"

    def build_app(self):
        """
        This method builds the provided app.
        :return: True if success else False
        """
        raise NotImplementedError("Build App not overridden.")

    def get_app_name(self):
        """
        Gets the name(main package name) of the app.
        :return: package name of the app
        """
        raise NotImplementedError("get app name Not implemented.")

    @staticmethod
    def install_apk(apk_path, target_device_handler):
        """
        Static helper method used to install the provided apk to corresponding device.
        :param apk_path: file path to the apk that needs to be installed.
        :param target_device_handler: Device handler of the corresponding device to install.
        :return: True if success else False
        """
        target_args = ['adb', '-s', target_device_handler.target_device_id, 'install', apk_path]
        ret_code, _, _ = run_command(target_args)
        return ret_code == 0

    def install_app(self, device_handler):
        """
        Install the app on the device
        :param device_handler:Device handler of the corresponding device to install.
        :return: True if success else False
        """
        raise NotImplementedError("Install App not overridden")

    def uninstall_app(self, target_device_handler):
        """
        Uninstall the app from the device.
        :param target_device_handler: Device handler of the corresponding device from which the app needs to be
        uninstalled.
        :return: True if success else False
        """
        target_args = ['adb', '-s', target_device_handler.target_device_id, 'uninstall', self.get_app_name()]
        ret_code, _, _ = run_command(target_args)
        return ret_code == 0

    def __str__(self):
        return self.get_name()
