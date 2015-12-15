#!/usr/bin/python
__author__ = 'machiry'
import sys
from property_parser import parse_properties_file
import property_parser
from ..app_handlers.apk_handler import ApkHandler
from ..app_handlers.app_src_handler import AppSrcHandler
from ..utils.logger import DDLogger
from test_profile import TestProfile
from ..test_harness.test_strategy import get_test_strategies
from ..device_handlers.device_manager import get_available_devices, get_free_device
from multiprocessing.pool import ThreadPool
import time
import os


def print_usage():
    print(sys.arv[0] + " <property_file>")


def get_all_profiles(properties_dict, target_log):
    target_test_profiles = []
    apps_dir = properties_dict[property_parser.APP_DIR_PROPERTY_NAME]
    base_work_dir = properties_dict[property_parser.WORK_DIR_PROPERTY_NAME]
    if not os.path.exists(apps_dir):
        target_log.log_failure("Provided Application Directory does not exist:" +
                               str(properties_dict[property_parser.APP_DIR_PROPERTY_NAME]))
    else:
        apps_with_src = []
        apks = []
        for curr_file in os.listdir(apps_dir):
            full_path = os.path.join(apps_dir, curr_file)
            if os.path.isfile(full_path):
                if full_path.endswith(".apk"):
                    apks.append(full_path)
                else:
                    target_log.log_warning("Ignoring non-APK file:" + full_path)
            else:
                apps_with_src.append(full_path)

        target_num_events = set(filter(lambda x: x.strip(),
                                       properties_dict[property_parser.EVENT_COUNT_PROPERTY_NAME].split(',')))

        all_test_strategies = set(filter(lambda x: x.strip(),
                                         properties_dict[property_parser.TEST_STRATEGY_PROPERTY_NAME].split(',')))

        all_selection_strategies = set(filter(lambda x: x.strip(),
                                              properties_dict[property_parser.SEL_STRATEGY_PROPERTY_NAME].split(',')))

        # First Create test profiles for all apks
        for curr_apk in apks:
            for curr_event_num in target_num_events:
                for curr_strategy in all_test_strategies:
                    all_strategy_objs = get_test_strategies(curr_strategy, all_selection_strategies)
                    for curr_strategy_obj in all_strategy_objs:
                        curr_app_work_dir = os.path.join(base_work_dir, os.path.basename(curr_apk) + '_' +
                                                         str(curr_event_num) + '_' + curr_strategy_obj)
                        curr_app_handler = ApkHandler(curr_apk, curr_app_work_dir)
                        curr_app_test_profile = TestProfile(curr_app_handler, curr_strategy_obj, int(curr_event_num),
                                                            {}, curr_app_work_dir)
                        target_test_profiles.append(curr_app_test_profile)

        # Second, create test profiles for all apps with sources
        for curr_app_src in apps_with_src:
            for curr_event_num in target_num_events:
                for curr_strategy in all_test_strategies:
                    all_strategy_objs = get_test_strategies(curr_strategy, all_selection_strategies)
                    for curr_strategy_obj in all_strategy_objs:
                        curr_app_work_dir = os.path.join(base_work_dir, os.path.basename(curr_app_src) + '_' +
                                                         str(curr_event_num) + '_' + curr_strategy_obj)
                        curr_app_handler = AppSrcHandler(curr_app_src, curr_app_work_dir)
                        curr_app_test_profile = TestProfile(curr_app_handler, curr_strategy_obj, int(curr_event_num),
                                                            {}, curr_app_work_dir)
                        target_test_profiles.append(curr_app_test_profile)

        return target_test_profiles


def run_test_profile(curr_test_profile, curr_log):
    target_device = get_free_device()
    while target_device is None:
        curr_log.log_info("Sleeping for test profile:" + str(curr_test_profile))
        time.sleep(5)
        target_device = get_free_device()
    curr_log.log_info("Got Device:" + str(target_device) + " For test profile:" + str(curr_test_profile))
    curr_test_profile.set_device(target_device)
    curr_log.log_info("Running Test Profile:" + str(curr_test_profile))
    curr_test_profile.run_profile()


def main():
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
    main_log.log_info("Got " + len(all_test_profiles) + " To Execute.")

    # 4. Execute each test profile.
    no_of_available_devices = get_available_devices()
    if no_of_available_devices <= 0:
        main_log.log_info("No Devices available to test.")
        return -3
    main_log.log_info("Identified " + str(no_of_available_devices) + " available devices.")
    all_test_profiles = map(lambda x: (x, main_log), all_test_profiles)
    main_log.log_info("Running all test profiles.")
    curr_pool = ThreadPool(processes=no_of_available_devices)
    curr_pool.map(run_test_profile, all_test_profiles)
    main_log.log_info("Scheduled all test profiles.")
    curr_pool.join()
    main_log.log_info("All Test Profiles Completed Execution.")


if __name__ == "__main__":
    sys.exit(main())
