__author__ = 'machiry'
from app_handler import AppHandler
from ..utils.logger import DDLogger
import os


class ApkHandler(AppHandler):

    def __init__(self, apk_full_path, target_log_dir):
        self.target_log_dir = target_log_dir
        if not os.path.exists(target_log_dir):
            self.target_log_dir = os.getcwd()
            DDLogger.write_failure_message("Directory provided for log is empty, using current directory:" +
                                           str(self.target_log_dir))
        assert os.path.exists(apk_full_path), "Provided APK:" + str(apk_full_path) + " does not exist."

        self.apk_full_path = apk_full_path
        self.logger = DDLogger(self.__class__.__name__,
                               target_log_file=os.path.join(self.target_log_dir, "apkHandler.log"),
                               exit_on_failure=True)

    def build_app(self):
        # Nothing to do for APK.
        return True

    def install_app(self, device_handler):
        """

        :param device_handler:
        :return:
        """
        return AppHandler.install_apk(self.apk_full_path, device_handler)

    def get_name(self):
        return "APK_" + str(self.apk_full_path)
