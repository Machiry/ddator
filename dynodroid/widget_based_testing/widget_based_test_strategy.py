__author__ = 'machiry'
from ..test_harness.test_strategy import TestStrategy
from ..utils.common_utils import create_dirs
from ..utils.logger import DDLogger
from ..utils.ui_helper import get_current_screen, get_current_package
from ..device_events.startapp_event import StartAppEvent
from ..device_events.event_helper import get_all_possible_ui_events
from frequency_based_selection import FrequencyBasedSelection
from random_bias_selection import RandomBiasSelection
from random_selection import RandomSelection
import random
import os


class WidgetBasedTesting(TestStrategy):
    """
    This class represents widget based test strategy.
    """

    STRATEGY_NAME = "WidgetBasedTesting"

    def __init__(self):
        self.selection_strategy = None
        self.target_device = None
        self.log_folder = None
        self.target_app_handler = None
        self.setup_complete = None
        self.number_of_events = None
        self.log = None

    @staticmethod
    def create_test_strategies(selection_strategies_name):
        """
        Given set of selection strategies, create TestStrategies with corresponding selection strategy.
        :param selection_strategies_name: names of selection strategies.
        :return: list of test strategy objects.
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

    def setup(self, target_device, log_folder, target_app_handler, number_of_events):
        setup_success = False
        assert target_device is not None, "Device provided should not be None"
        assert log_folder is not None, "log folder should not be None"
        assert target_app_handler is not None, "App handler should not be None"
        assert number_of_events > 0, "Number of events should be greater than 0"
        self.number_of_events = number_of_events
        self.target_device = target_device
        self.target_app_handler = target_app_handler
        create_dirs(log_folder)
        self.log = DDLogger(self.__class__.__name__, target_log_file=os.path.join(log_folder, self.get_name() + ".log"))
        self.log.log_info("Starting to Reset Device:" + str(self.target_device))
        if self.target_device.reset_device():
            self.log.log_info("Resetting Device Successful:" + str(self.target_device))
        else:
            self.log.log_failure("Failed to Reset Device:" + str(self.target_device))
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
        return WidgetBasedTesting.STRATEGY_NAME + '_' + \
               (self.selection_strategy.get_name() if self.selection_strategy is not None else "")

    def run_tests(self):
        to_ret = False
        if self.setup_complete is None:
            DDLogger.write_failure_message("Set up is not called:" + self.get_name())
        elif not self.setup_complete:
            self.log.log_failure("Setup failed, Not Running Tests.")
        else:
            to_ret = False
            self.log.log_info("Starting to Run Tests.")
            start_app = StartAppEvent(self.target_app_handler.manifest_info['package_name'],
                                      self.target_app_handler.manifest_info['main_activity'])
            # start the app
            if start_app.trigger_event(self.target_device, self.log):
                to_ret = True
                self.log.log_info("Started App:" + str(self.target_app_handler) + " successfully")
                # get current screen.
                old_screen = get_current_screen(self.target_device)
                self.selection_strategy.update_new_screen(old_screen)
                curr_event_number = 0
                while curr_event_number < self.number_of_events:
                    # get next widget
                    target_widget = self.selection_strategy.get_next_widget()
                    if target_widget is None:
                        self.log.log_warning("No widgets to click on the Application")
                        break
                    possible_events = get_all_possible_ui_events(target_widget)
                    if len(possible_events) > 0:
                        # pick a random event to trigger on the widget
                        target_event = random.choice(possible_events)
                        # trigger the event
                        if target_event and target_event.trigger_event(self.target_device, self.log):
                            curr_event_number += 1
                            self.log.log_info("Performed Event:" + str(target_event))
                        else:
                            self.log.log_failure("Failed to perform event:" + str(target_event))
                        curr_screen = get_current_screen(self.target_device)
                        current_pkg = get_current_package(self.target_device)
                        # if the app exited? Restart the app
                        if current_pkg != self.target_app_handler.get_app_name():
                            start_app.trigger_event(self.target_device, self.log)
                        # if new screen is seen, update the selection strategy with corresponding info.
                        if curr_screen != old_screen:
                            self.selection_strategy.update_new_screen(curr_screen)
            else:
                self.log.log_failure("Failed to Start App:" + str(self.target_app_handler))

        return to_ret

    def cleanup(self):
        # clean up
        # uninstall the app
        to_ret = self.target_app_handler.uninstall_app(self.target_device)
        if to_ret:
            self.log.log_info("Uninstalled App:" + str(self.target_app_handler) + " Successfully.")
        else:
            self.log.log_failure("Failed to uninstall App:" + str(self.target_app_handler))
        return to_ret
