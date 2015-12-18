__author__ = 'machiry'
from ..test_harness.test_strategy import TestStrategy
from ..utils.common_utils import create_dirs
from ..utils.logger import DDLogger
from ..device_events.StartAppEvent import StartAppEvent
from frequency_based_selection import FrequencyBasedSelection
from random_bias_selection import RandomBiasSelection
from random_selection import RandomSelection
import os


class WidgetBasedTesting(TestStrategy):

    STRATEGY_NAME = "WidgetBasedTesting"

    def __init__(self):
        self.selection_strategy = None
        self.target_device = None
        self.log_folder = None
        self.target_app_handler = None
        self.setup_complete = None
        self.log = None

    @staticmethod
    def create_test_strategies(selection_strategies_name):
        """

        :param selection_strategies_name:
        :return:
        """

        to_return_strategies = []
        for curr_sel_strategy in selection_strategies_name:
            target_obj = None
            if curr_sel_strategy == RandomSelection.get_selection_name():
                target_obj = RandomSelection()
            if curr_sel_strategy == RandomBiasSelection.get_selection_name():
                target_obj = RandomBiasSelection()
            if curr_sel_strategy == FrequencyBasedSelection.get_selection_name():
                target_obj = FrequencyBasedSelection()
            if target_obj is not None:
                widget_testing = WidgetBasedTesting()
                widget_testing.selection_strategy = target_obj
                to_return_strategies.append(widget_testing)
            else:
                DDLogger.write_failure_message("Invalid Selection strategy name provided:" +
                                               str(curr_sel_strategy))
        return to_return_strategies

    def setup(self, target_device, log_folder, target_app_handler):
        setup_success = False
        assert target_device is not None, "Device provided should not be None"
        assert log_folder is not None, "log folder should not be None"
        assert target_app_handler is not None, "App handler should not be None"
        self.target_device = target_device
        self.target_app_handler = target_app_handler
        create_dirs(log_folder)
        self.log = DDLogger(self.__class__.__name__, target_log_file=os.path.join(log_folder, self.get_name() + ".log"))
        self.log.log_info("Starting to Reset Device:" + str(self.target_device))
        """if self.target_device.reset_device():
            self.log.log_info("Resetting Device Successful:" + str(self.target_device))
        else:
            self.log.log_failure("Failed to Reset Device:" + str(self.target_device))"""
        if self.target_app_handler.build_app():
            self.log.log_info("Successfully Built Application:" + str(self.target_app_handler))
        else:
            self.log.log_failure("Failed to Build Application:" + str(self.target_app_handler))
        self.log.log_info("Trying to install application:" + str(self.target_app_handler) + " on device:" +
                          str(self.target_device))
        setup_success = self.target_app_handler.install_app(self.target_device)
        if not setup_success:
            self.log.log_failure("Installation of APK:" + str(self.target_app_handler) + " Failed on Device:" +
                                 str(self.target_device))
        else:
            self.log.log_info("Installation Successful.")
        self.setup_complete = setup_success
        return self.setup_complete

    def get_name(self):
        # TODO: Fix this
        return WidgetBasedTesting.STRATEGY_NAME + '_' # + self.selection_strategy.get_name()

    def run_tests(self):
        to_ret = False
        if self.setup_complete is None:
            DDLogger.write_failure_message("Set up is not called:" + self.get_name())
        elif not self.setup_complete:
            self.log.log_failure("Setup failed, Not Running Tests.")
        else:
            to_ret = True
            self.log.log_info("Starting to Run Tests.")
            start_app = StartAppEvent(self.target_app_handler.manifest_info['package_name'],
                                      self.target_app_handler.manifest_info['main_activity'])
            if start_app.trigger_event(self.target_device, self.log):
                self.log.log_info("Started App:" + str(self.target_app_handler) + " successfully")

        return to_ret

    def cleanup(self):
        to_ret = self.target_app_handler.uninstall_app(self.target_device)
        if to_ret:
            self.log.log_info("Uninstalled App:" + str(self.target_app_handler) + " Successfully.")
        else:
            self.log.log_failure("Failed to uninstall App:" + str(self.target_app_handler))
        return to_ret
