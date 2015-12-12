__author__ = 'machiry'
from app_handler import AppHandler
from ..utils.logger import DDLogger
import os


class AppSrcHandler(AppHandler):

    def __init__(self, app_full_path, target_log_dir):
        self.target_log_dir = target_log_dir
        if not os.path.exists(target_log_dir):
            self.target_log_dir = os.getcwd()
            DDLogger.write_failure_message("Directory provided for log is empty, using current directory:" +
                                           str(self.target_log_dir))
        assert os.path.exists(app_full_path), "Provided APP Path:" + str(app_full_path) + " does not exist."

        self.app_full_path = app_full_path
        self.logger = DDLogger(self.__class__.__name__,
                               target_log_file=os.path.join(self.target_log_dir, "appSrcHandler.log"),
                               exit_on_failure=True)

    def build_app(self):
        # TODO: build the app with sources
        return True
