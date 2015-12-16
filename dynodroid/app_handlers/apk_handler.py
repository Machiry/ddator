__author__ = 'machiry'
from app_handler import AppHandler
from ..utils.logger import DDLogger
from ..utils.apk_utils import decompress_apk
from ..utils.manifest_handler import parse_apk_manifest
from ..utils.common_utils import create_dirs
import os


class ApkHandler(AppHandler):

    def __init__(self, apk_full_path, target_log_dir):
        self.target_log_dir = target_log_dir
        if not os.path.exists(target_log_dir):
            create_dirs(self.target_log_dir)
        assert os.path.exists(apk_full_path), "Provided APK:" + str(apk_full_path) + " does not exist."
        self.extracted_apk_dir = os.path.join(self.target_log_dir, "extracted_apk_dir")
        self.apk_full_path = apk_full_path
        assert decompress_apk(self.apk_full_path, self.extracted_apk_dir), "Failed to Decompress APK:" + \
                                                                           self.apk_full_path + ", Probably a Bad APK"
        self.manifest_fp = os.path.join(self.extracted_apk_dir, "AndroidManifest.xml")
        self.manifest_info = parse_apk_manifest(self.manifest_fp)
        assert len(self.manifest_info) > 0, "Unable to parse manifest:" + str(self.manifest_fp)
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

    def get_app_name(self):
        return self.manifest_info["package_name"]

    def get_name(self):
        return "APK_" + str(self.apk_full_path)
