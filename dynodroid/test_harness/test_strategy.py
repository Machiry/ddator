__author__ = 'machiry'


class TestStrategy(object):
    """
    A generic test strategy.
    An abstract class, which all test strategies should inherit.
    It has set of methods that need to be implemented by any test strategy.
    """

    def setup(self, target_device, log_folder, target_app_handler, number_of_events):
        """
        Set up the device to run the test strategy.
        This is the first method, to be run on any test strategy.
        This setups the device to run tests.
        Note: This method should pass for the test strategy to be run.

        :param target_device: Device on which the strategy should be run.
        :param log_folder: folder to be used for all the logging.
        :param target_app_handler: Handler for the app to test.
        :param number_of_events: Number of events that should be trigerred on the app.
        :return: True/False => success/failure.
        """
        raise NotImplementedError("setup not overridden.")

    def get_name(self):
        return "TestStrategy"

    def run_tests(self):
        """
        Perform testing, run all the tests.
        :return: True/False => success/failure
        """
        raise NotImplementedError("run tests not overridden.")

    def cleanup(self):
        """
        Clean up the device.
        This method should always be run after setup and before releasing the device.
        :return: True/False => success/failure
        """
        raise NotImplementedError("Clean up not overridden.")

    def __str__(self):
        return self.get_name()
