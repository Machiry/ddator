__author__ = 'machiry'
from dynodroid.utils.common_utils import create_dirs

"""

"""


class TestProfile:

    def __init__(self, target_app_config, test_strategy, number_of_events, strategy_params, log_folder):
        """

        :param target_app_config:
        :param test_strategy:
        :param number_of_events:
        :param strategy_params:
        :param log_folder:
        :return:
        """
        TestProfile._validate_params(target_app_config, test_strategy, number_of_events, strategy_params, log_folder)
        self.target_app_config = target_app_config
        self.test_strategy = test_strategy
        self.number_of_events = number_of_events
        self.strategy_prams = strategy_params
        self.log_folder = log_folder
        self.target_device = None
        create_dirs(log_folder)

    def set_device(self, target_device):
        assert target_device is not None, "Device to test on cannot be None."
        self.target_device = target_device

    def run_profile(self):
        # TODO code to execute tests.
        pass

    @staticmethod
    def _validate_params(target_app_config, test_strategy, number_of_events, strategy_params, log_folder):
        """

        :param target_app_config:
        :param test_strategy:
        :param number_of_events:
        :param strategy_params:
        :param log_folder:
        :return:
        """
        assert target_app_config is not None, "Appconfig cannot be None"
        assert test_strategy is not None, "Test strategy cannot be None"
        assert number_of_events is not None, "Number of events cannot be None"
        assert strategy_params is not None, "Strategy parameters cannot be None"
        assert log_folder is not None, "Log folder cannot be None"
