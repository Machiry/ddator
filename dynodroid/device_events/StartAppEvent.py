from system_event import SystemEvent


class StartAppEvent(SystemEvent):
    """

    """
    def __init__(self, app_pkg_name, main_activity_name):
        self.app_pkg_name = app_pkg_name
        self.main_activity_name = main_activity_name

    def get_adb_args(self):
        adb_args = ['shell', 'am', 'start', '-n', self.app_pkg_name + '/' + self.main_activity_name]
        return adb_args

    def get_name(self):
        return "StartAppSystemEvent_" + str(self.app_pkg_name) + '/' + str(self.main_activity_name)

    def trigger_event(self, target_device, target_logger):
        target_device.get_ui_handle().wakeup()
        starting_success = super(StartAppEvent, self).trigger_event(target_device, target_logger)
        if starting_success:
            curr_info = target_device.get_ui_handle().info
            if (curr_info is not None) and ('currentPackageName' in curr_info):
                starting_success = (curr_info['currentPackageName'] == self.app_pkg_name)
        return starting_success


