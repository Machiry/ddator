__author__ = 'machiry'
from ..utils.common_utils import read_file_lines
from ..utils.logger import DDLogger

PROPERTIES_DICT = \
    {"work_dir": "Directory where all logs, stats and other output from Dynodroid will be saved.",
        "sdk_install": "Directory where Android SDK is expected to present.",
        "app_dir": "Directory where all apps that need to be tested are present.",
        "test_strategy": "Comma separated list of test strategies that need to be used.",
        "sel_strategy": "Comma separated list of widget selection strategies that need to "
                         "be used (applicable only if test_strategy = WidgetBasedTesting",
        "max_widgets": "Maximum number of widgets that need to be exercised.",
        "cov_sample": "Number of events after which coverage need to be collected.",
        "avd_store": "Path where created emulators need to be stored.",
        "event_count": "Number of events that need to be used for testing.",
        "apktool_loc": "Absolute path of apktool.jar.",
        "max_emu": "Maximum number of emulators that could be used for testing.",
        "complete_notify": "Email id to which a message need to be sent when complete running is done.",
        "report_email_user": "Email id(gmail) which should be used as source to send email.",
        "report_email_pass": "Password of the report email id."}

parsed_properties = dict()


def get_properties():
    """

    :return:
    """
    assert len(parsed_properties) > 0, "Properties not parsed. Parse the properties file, before calling this method."
    return dict(parsed_properties)


def parse_properties_file(property_file):
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
