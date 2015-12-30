from system_event import SystemEvent


class BatteryChanged(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + BatteryChanged.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.BATTERY_CHANGED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', BatteryChanged.get_name()]


class BatteryLow(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + BatteryLow.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.BATTERY_LOW"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', BatteryLow.get_name()]


class BatteryOkay(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + BatteryOkay.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.BATTERY_OKAY"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', BatteryOkay.get_name()]


class AppWidgetUpdate(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + AppWidgetUpdate.get_name()

    @staticmethod
    def get_name():
        return "android.appwidget.action.APPWIDGET_UPDATE"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', AppWidgetUpdate.get_name()]


class AudioBecomingNoisy(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + AudioBecomingNoisy.get_name()

    @staticmethod
    def get_name():
        return "android.media.AUDIO_BECOMING_NOISY"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', AudioBecomingNoisy.get_name()]


class BootCompleted(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + BootCompleted.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.BOOT_COMPLETED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', BootCompleted.get_name()]


class ConnectivityChange(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + ConnectivityChange.get_name()

    @staticmethod
    def get_name():
        return "android.net.conn.CONNECTIVITY_CHANGE"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', ConnectivityChange.get_name()]


class DateChanged(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + DateChanged.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.DATE_CHANGED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', DateChanged.get_name()]


class InputMethodChanged(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + InputMethodChanged.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.INPUT_METHOD_CHANGED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', InputMethodChanged.get_name()]


class MediaEject(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + MediaEject.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.MEDIA_EJECT"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', MediaEject.get_name()]


class MediaMounted(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + MediaMounted.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.MEDIA_MOUNTED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', MediaMounted.get_name()]


class MediaScannerFinished(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + MediaScannerFinished.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.MEDIA_SCANNER_FINISHED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', MediaScannerFinished.get_name()]


class MediaUnmounted(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + MediaUnmounted.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.MEDIA_UNMOUNTED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', MediaUnmounted.get_name()]


class NewOutgoingCall(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + NewOutgoingCall.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.NEW_OUTGOING_CALL"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', NewOutgoingCall.get_name()]


class PackageAdded(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + PackageAdded.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.PACKAGE_ADDED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', PackageAdded.get_name()]


class PackageRemoved(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + PackageRemoved.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.PACKAGE_REMOVED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', PackageRemoved.get_name()]


class PackageReplaced(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + PackageReplaced.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.PACKAGE_REPLACED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', PackageReplaced.get_name()]


class PowerConnected(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + PowerConnected.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.ACTION_POWER_CONNECTED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', PowerConnected.get_name()]


class PowerDisconnected(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + PowerDisconnected.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.ACTION_POWER_DISCONNECTED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', PowerDisconnected.get_name()]


class ShutdownAction(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + ShutdownAction.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.ACTION_SHUTDOWN"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', ShutdownAction.get_name()]


class TimeSetAction(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + TimeSetAction.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.TIME_SET"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', TimeSetAction.get_name()]


class TimeZoneChanged(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + TimeZoneChanged.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.TIMEZONE_CHANGED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', TimeZoneChanged.get_name()]


class UMSConnected(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + UMSConnected.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.UMS_CONNECTED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', UMSConnected.get_name()]


class UMSDisconnected(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + UMSDisconnected.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.UMS_DISCONNECTED"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', UMSDisconnected.get_name()]


class UserPresentAction(SystemEvent):
    """

    """

    def __init__(self, intent_filters_category):
        self.intent_filters_category = list(intent_filters_category)

    def __str__(self):
        return "BROADCAST_" + UserPresentAction.get_name()

    @staticmethod
    def get_name():
        return "android.intent.action.USER_PRESENT"

    def get_adb_args(self):
        return ['shell', 'am', 'broadcast', '-a', UserPresentAction.get_name()]