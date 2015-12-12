__author__ = 'machiry'
from ..test_harness.test_strategy import TestStrategy


class WidgetBasedTesting(TestStrategy):

    STRATEGY_NAME = "WidgetBasedTesting"

    def __init__(self):
        self.selection_strategy = None
        pass

    @staticmethod
    def create_test_strategies(selection_strategies_name):
        """

        :param selection_strategies_name:
        :return:
        """
        to_return_strategies = []
        for curr_sel_strategy in selection_strategies_name:
            # TODO: Create a TestingObject based on selection strategy.
            pass
        return to_return_strategies

    def setup(self):
        raise NotImplementedError("setup not overridden.")

    def get_name(self):
        return WidgetBasedTesting.STRATEGY_NAME + '_' + self.selection_strategy.get_name()

    def run_tests(self):
        raise NotImplementedError("run tests not overridden.")

    def cleanup(self):
        raise NotImplementedError("Clean up not overridden.")
