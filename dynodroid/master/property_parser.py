__author__ = 'machiry'
from ..utils.common_utils import read_file_lines
from ..utils.logger import DDLogger

WORK_DIR_PROPERTY_NAME = "work_dir"
SDK_INSTALL_PROPERTY_NAME = "sdk_install"
APP_DIR_PROPERTY_NAME = "app_dir"
TEST_STRATEGY_PROPERTY_NAME = "test_strategy"
SEL_STRATEGY_PROPERTY_NAME = "sel_strategy"
MAX_WIDGETS_PROPERTY_NAME = "max_widgets"
COV_SAMPLE_PROPERTY_NAME = "cov_sample"
EVENT_COUNT_PROPERTY_NAME = "event_count"
DEVICE_ID_PROPERTY_NAME = "device_ids"
COMPLETE_NOTIFY_PROPERTY_NAME = "complete_notify"
REPORT_EMAIL_USER_PROPERTY_NAME = "report_email_user"
REPORT_EMAIL_PASS_PROPERTY_NAME = "report_email_pass"

PROPERTIES_DICT = \
    {WORK_DIR_PROPERTY_NAME: "Directory where all logs, stats and other output from Dynodroid will be saved.",
        SDK_INSTALL_PROPERTY_NAME: "Directory where Android SDK is expected to present.",
        APP_DIR_PROPERTY_NAME: "Directory where all apps that need to be tested are present.",
        TEST_STRATEGY_PROPERTY_NAME: "Comma separated list of test strategies that need to be used.",
        SEL_STRATEGY_PROPERTY_NAME: "Comma separated list of widget selection strategies that need to "
                                    "be used (applicable only if test_strategy = WidgetBasedTesting",
        MAX_WIDGETS_PROPERTY_NAME: "Maximum number of widgets that need to be exercised.",
        COV_SAMPLE_PROPERTY_NAME: "Number of events after which coverage need to be collected.",
        EVENT_COUNT_PROPERTY_NAME: "Number of events that need to be used for testing.",
        DEVICE_ID_PROPERTY_NAME: "Comma separated list of device ids that should be used for testing",
        COMPLETE_NOTIFY_PROPERTY_NAME: "Email id to which a message need to be sent when complete running is done.",
        REPORT_EMAIL_USER_PROPERTY_NAME: "Email id(gmail) which should be used as source to send email.",
        REPORT_EMAIL_PASS_PROPERTY_NAME: "Password of the report email id."}

parsed_properties = dict()


def get_properties():
    """

    :return:
    """
    assert len(parsed_properties) > 0, "Properties not parsed. Parse the properties file, before calling this method."
    return dict(parsed_properties)


def parse_properties_file(property_file):
    """

    :param property_file:
    :return:
    """
    if len(parsed_properties) == 0:
        file_lines = read_file_lines(property_file)
        for curr_line in file_lines:
            # If the current line is not comment
            if not curr_line.startswith('#'):
                property_pair = curr_line.split('=')
                if len(property_pair) == 2:
                    key_name = property_pair[0].strip()
                    value_name = property_pair[1].strip()
                    parsed_properties[key_name] = value_name
        for curr_key in PROPERTIES_DICT:
            if curr_key not in parsed_properties:
                # TODO: consider default values for these keys.
                DDLogger.write_failure_message("Property " + curr_key + "(" + PROPERTIES_DICT[curr_key] +
                                               ") not specified.")
    return parsed_properties
