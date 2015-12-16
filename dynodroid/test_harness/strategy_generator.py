from ..widget_based_testing.widget_based_test_strategy import WidgetBasedTesting


def get_test_strategies(strategy_name, strategy_params):
    """

    :param strategy_name:
    :param strategy_params:
    :return:
    """
    if strategy_name == WidgetBasedTesting.STRATEGY_NAME:
        return WidgetBasedTesting.create_test_strategies(strategy_params)