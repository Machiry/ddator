__author__ = 'machiry'
from dynodroid.utils.common_utils import create_dirs

"""

"""


class TestProfile:

    def __init__(self, target_app_config, test_strategy_name, strategy_params, log_folder):
        """

        :param target_app_config:
        :param test_strategy_name:
        :param strategy_params:
        :param log_folder:
        :return:
        """
        TestProfile._validate_params(target_app_config, test_strategy_name, strategy_params, log_folder)
        self.target_app_config = target_app_config
        self.test_strategy_name = test_strategy_name
        self.strategy_prams = strategy_params
        self.log_folder = log_folder
        create_dirs(log_folder)

    @staticmethod
    def _validate_params(target_app_config, test_strategy_name, strategy_params, log_folder):
        """

        :param target_app_config:
        :param test_strategy_name:
        :param strategy_params:
        :param log_folder:
        :return:
        """
        assert target_app_config is not None, "Appconfig cannot be None"
        assert test_strategy_name is not None, "Test strategy name cannot be None"
        assert strategy_params is not None, "strategy params cannot be None"
        assert log_folder is not None, "Log folder cannot be None"
