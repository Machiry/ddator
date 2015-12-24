#!/usr/bin/python
__author__ = 'machiry'
import sys
from property_parser import parse_properties_file
import property_parser
from ..app_handlers.app_handler_helper import get_app_handler
from ..utils.logger import DDLogger
from test_profile import TestProfile
from ..test_harness.strategy_generator import get_test_strategies
from ..device_handlers.device_manager import get_available_devices, get_free_device, put_free_device
from multiprocessing.pool import ThreadPool
import time
import os


def print_usage():
    """
    Print usage of the framework on stdin
    :return: None
    """
    print(sys.argv[0] + " <property_file>")


def get_all_profiles(properties_dict, target_log):
    """
    This method computes all possible test profiles that need to run based on the provided properties.
    :param properties_dict: Dictionary containing all the properties.
    :param target_log: logger to log failure.
    :return: list containing all possible test profile objects that need to be scheduled.
    """
    target_test_profiles = []
    apps_dir = properties_dict[property_parser.APP_DIR_PROPERTY_NAME]
    base_work_dir = properties_dict[property_parser.WORK_DIR_PROPERTY_NAME]
    # check appd directory
    if not os.path.exists(apps_dir):
        target_log.log_failure("Provided Application Directory does not exist:" +
                               str(properties_dict[property_parser.APP_DIR_PROPERTY_NAME]))
    else:
        # get absolute path of all apps
        apps_path = map(lambda x: os.path.join(apps_dir, x), os.listdir(apps_dir))

        # get all event numbers.
        target_num_events = set(filter(lambda x: x.strip(),
                                       properties_dict[property_parser.EVENT_COUNT_PROPERTY_NAME].split(',')))

        # get all test strategies
        all_test_strategies = set(filter(lambda x: x.strip(),
                                         properties_dict[property_parser.TEST_STRATEGY_PROPERTY_NAME].split(',')))

        # get all selection strategies
        all_selection_strategies = set(filter(lambda x: x.strip(),
                                              properties_dict[property_parser.SEL_STRATEGY_PROPERTY_NAME].split(',')))
        # Bad apps: apps we do not know how to handle.
        bad_apps_path = set()
        # Create test profiles for all apps
        for curr_app_path in apps_path:
            # for each app
            for curr_event_num in target_num_events:
                # for each event number
                for curr_strategy in all_test_strategies:
                    # for each strategy
                    all_strategy_objs = get_test_strategies(curr_strategy, all_selection_strategies)
                    for curr_strategy_obj in all_strategy_objs:
                        curr_app_work_dir = os.path.join(base_work_dir, os.path.basename(curr_app_path) + '_' +
                                                         str(curr_event_num) + '_' + str(curr_strategy_obj))
                        curr_app_handler = get_app_handler(curr_app_path, curr_app_work_dir)
                        if curr_app_handler is None:
                            bad_apps_path.add(curr_app_path)
                        else:
                            curr_app_test_profile = TestProfile(curr_app_handler, curr_strategy_obj, int(curr_event_num),
                                                                {}, curr_app_work_dir)
                            target_test_profiles.append(curr_app_test_profile)

        for bad_app_path in bad_apps_path:
            target_log.log_failure("No App Handler found for:" + str(bad_app_path) + '. Ignoring.')

        return target_test_profiles


def run_test_profile(curr_pair):
    """
    Run the provided test profile.
    :param curr_pair: (test_profile, logger) : tuple containing test profile to run and logger,
    that needs to be used for logging.
    :return: None
    """
    curr_test_profile = curr_pair[0]
    curr_log = curr_pair[1]
    # get free device
    target_device = get_free_device()
    # wait till we get a free device
    while target_device is None:
        curr_log.log_info("Sleeping for test profile:" + str(curr_test_profile))
        time.sleep(5)
        target_device = get_free_device()
    # run the test profile
    curr_log.log_info("Got Device:" + str(target_device) + " For test profile:" + str(curr_test_profile))
    curr_test_profile.set_device(target_device)
    curr_log.log_info("Running Test Profile:" + str(curr_test_profile))
    curr_test_profile.run_profile()
    # release the device
    put_free_device(target_device)


def master():
    # 1. Check args
    if len(sys.argv) < 2:
        print_usage()
        return -1
    # 2. Parse property file
    if not os.path.exists(sys.argv[1]):
        print("Provided Properties file does not exist:" + str(sys.arv[1]))
        return -2
    current_properties = parse_properties_file(sys.argv[1])
    main_log = DDLogger("Main_Class",
                        target_log_file=os.path.join(current_properties[property_parser.WORK_DIR_PROPERTY_NAME],
                                                     "main_log.log"), exit_on_failure=True)
    main_log.log_info("Got all properties.")
    # 3. Get various test profiles.
    all_test_profiles = get_all_profiles(current_properties, main_log)
    main_log.log_info("Got " + str(len(all_test_profiles)) + " To Execute.")

    # 4. Execute each test profile.
    no_of_available_devices = get_available_devices()
    if no_of_available_devices <= 0:
        main_log.log_info("No Devices available to test.")
        return -3
    main_log.log_info("Identified " + str(no_of_available_devices) + " available devices.")
    all_test_profiles = map(lambda x: (x, main_log), all_test_profiles)
    main_log.log_info("Running all test profiles.")
    # As number of test profile to run simultaneously depend on number of devices.
    # create thread pool with number of threads equal to number of devices.
    curr_pool = ThreadPool(processes=no_of_available_devices)
    curr_pool.map(run_test_profile, all_test_profiles)
    main_log.log_info("Scheduled all test profiles.")
    main_log.log_info("All Test Profiles Completed Execution.")
