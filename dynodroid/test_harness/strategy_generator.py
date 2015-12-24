from ..widget_based_testing.widget_based_test_strategy import WidgetBasedTesting


def get_test_strategies(strategy_name, strategy_params):
    """
    Generate test strategies depending on the provided strategy name and staretegy params.
    :param strategy_name: Name of the strategy to be used.
    :param strategy_params: parameters for the strategy.
    :return: List containing strategy opbjects.
    """
    if strategy_name == WidgetBasedTesting.STRATEGY_NAME:
        return WidgetBasedTesting.create_test_strategies(strategy_params)