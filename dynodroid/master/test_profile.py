__author__ = 'machiry'
from dynodroid.utils.common_utils import create_dirs
from ..utils.logger import DDLogger
import os


class TestProfile(object):
    """
    This class encapsulates a test profile.
    Test profile is a testing setup. It basically includes an app, device, and test strategy.
    """

    def __init__(self, target_app_handler, test_strategy, number_of_events, strategy_params, log_folder):
        """
        Create a test profile object.
        :param target_app_handler: App handler for the app to test.
        :param test_strategy: Test strategy to be used on the app.
        :param number_of_events: Number of events to test the app with.
        :param strategy_params: parameters for the test strategy.
        :param log_folder: folder to be used for all logging.
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
        """
        Set the provided device as test device.
        :param target_device: Device on which the test profile needs to run
        :return: None
        """
        assert target_device is not None, "Device to test on cannot be None."
        self.target_device = target_device

    def run_profile(self):
        """
        Run the profile.
        :return: None
        """
        assert self.target_device is not None, "First set the device"
        self.log.log_info("Starting to run test on Device:" + str(self.target_device))
        # Run setup
        if self.test_strategy.setup(self.target_device, os.path.join(self.log_folder, "test_strategy_log"),
                                    self.target_app_handler, self.number_of_events):
            self.log.log_info("Test Strategy:" + str(self.test_strategy) + " Setup Complete.")
            # Run tests, log any exceptions
            try:
                if self.test_strategy.run_tests():
                    self.log.log_info("Successfully Completed Running Tests.")
                else:
                    self.log.log_failure("Failed to Run tests.")
            except Exception as e:
                self.log.log_failure("Exception occurred while trying to run tests:" + e.message)
            # clean up
            try:
                if self.test_strategy.cleanup():
                    self.log.log_info("Successfully cleaned up.")
                else:
                    self.log.log_failure("Failed to clean up.")
            except Exception as e:
                self.log.log_failure("Exception occurred while trying to clean up:" + e.message)
        else:
            self.log.log_failure("Test Strategy:" + str(self.test_strategy) + " Setup Failed.")

    @staticmethod
    def _validate_params(target_app_handler, test_strategy, number_of_events, strategy_params, log_folder):
        """
        Validate all the provided parameters.
        :param target_app_handler: app handler of the app to test.
        :param test_strategy: test strategy object, that needs to be used for testing.
        :param number_of_events: Number of events to trigger.
        :param strategy_params: parameters for the strategy
        :param log_folder: folder where all logs need to be stored.
        :return: None
        """
        assert target_app_handler is not None, "AppHandler cannot be None"
        assert test_strategy is not None, "Test strategy cannot be None"
        assert number_of_events is not None, "Number of events cannot be None"
        assert strategy_params is not None, "Strategy parameters cannot be None"
        assert log_folder is not None, "Log folder cannot be None"

    def __str__(self):
        to_ret = "TestProfile_" + str(self.test_strategy) + "_" + \
                 ("" if self.target_device is None else str(self.target_device))
        return to_ret
