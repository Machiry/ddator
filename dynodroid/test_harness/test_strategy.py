__author__ = 'machiry'
from ..widget_based_testing.widget_based_test_strategy import WidgetBasedTesting


def get_test_strategies(strategy_name, strategy_params):
    """

    :param strategy_name:
    :param strategy_params:
    :return:
    """
    if strategy_name == WidgetBasedTesting.STRATEGY_NAME:
        return WidgetBasedTesting.create_test_strategies(strategy_params)


class TestStrategy:

    def setup(self, target_device):
        raise NotImplementedError("setup not overridden.")

    def get_name(self):
        raise NotImplementedError("get_name not overridden.")

    def run_tests(self):
        raise NotImplementedError("run tests not overridden.")

    def cleanup(self):
        raise NotImplementedError("Clean up not overridden.")