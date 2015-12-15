__author__ = 'machiry'
from dynodroid.utils.common_utils import create_dirs
from ..utils.logger import DDLogger
import os


class TestProfile:
    """

    """

    def __init__(self, target_app_handler, test_strategy, number_of_events, strategy_params, log_folder):
        """

        :param target_app_handler:
        :param test_strategy:
        :param number_of_events:
        :param strategy_params:
        :param log_folder:
        :return:
        """
        TestProfile._validate_params(target_app_handler, test_strategy, number_of_events, strategy_params, log_folder)
        self.target_app_handler = target_app_handler
        self.test_strategy = test_strategy
        self.number_of_events = number_of_events
        self.strategy_prams = strategy_params
        self.log_folder = log_folder
        self.target_device = None
        create_dirs(log_folder)
        self.log = DDLogger(self.__class__.__name__, target_log_file=os.path.join(log_folder, "test_profile_log.log"))

    def set_device(self, target_device):
        assert target_device is not None, "Device to test on cannot be None."
        self.target_device = target_device

    def run_profile(self):
        assert self.target_device is not None, "First set the device"
        self.log.log_info("Starting to run test on Device:" + str(self.target_device))
        if self.test_strategy.setup(self.target_device):
            self.log.log_info("Test Strategy:" + str(self.test_strategy) + " Setup Complete.")
            if self.test_strategy.run_tests():
                self.log.log_info("Successfully Completed Running Tests.")
            else:
                self.log.log_failure("Failed to Run tests.")
            if self.test_strategy.cleanup():
                self.log.log_info("Successfully cleaned up.")
            else:
                self.log.log_failure("Failed to clean up.")
        else:
            self.log.log_failure("Test Strategy:" + str(self.test_strategy) + " Setup Failed.")

    @staticmethod
    def _validate_params(target_app_handler, test_strategy, number_of_events, strategy_params, log_folder):
        """

        :param target_app_handler:
        :param test_strategy:
        :param number_of_events:
        :param strategy_params:
        :param log_folder:
        :return:
        """
        assert target_app_handler is not None, "AppHandler cannot be None"
        assert test_strategy is not None, "Test strategy cannot be None"
        assert number_of_events is not None, "Number of events cannot be None"
        assert strategy_params is not None, "Strategy parameters cannot be None"
        assert log_folder is not None, "Log folder cannot be None"
