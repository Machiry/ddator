__author__ = 'machiry'
from app_handler import AppHandler
from ..utils.logger import DDLogger
from ..utils.common_utils import create_dirs
import os


class AppSrcHandler(AppHandler):

    def __init__(self, app_full_path, target_log_dir):
        self.target_log_dir = target_log_dir
        if not os.path.exists(target_log_dir):
            create_dirs(self.target_log_dir)
        assert os.path.exists(app_full_path), "Provided APP Path:" + str(app_full_path) + " does not exist."

        self.app_full_path = app_full_path
        self.logger = DDLogger(self.__class__.__name__,
                               target_log_file=os.path.join(self.target_log_dir, "appSrcHandler.log"),
                               exit_on_failure=True)

    def build_app(self):
        # TODO: build the app with sources
        return True

    def install_app(self, device_handler):
        raise NotImplementedError("Install App not overridden")

    def get_app_name(self):
        raise NotImplementedError("get app name Not implemented.")

    def get_name(self):
        return "APPSRC_" + str(self.app_full_path)
