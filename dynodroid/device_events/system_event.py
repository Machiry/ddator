from generic_event import GenericEvent
from ..utils.common_utils import run_command
import time


class SystemEvent(GenericEvent):

    SYSTEM_EVENT_SLEEP_TIME = 2

    def get_adb_args(self):
        raise NotImplementedError("get adb args Not Implemented.")

    def get_name(self):
        return "GenericSystemEvent"

    def trigger_event(self, target_device, target_logger):
        trigger_args = ['adb', '-s', target_device.target_device_id]
        trigger_args.extend(self.get_adb_args())
        ret_code, output_text, error_text = run_command(trigger_args)
        if ret_code != 0:
            target_logger.log_failure("Failure occurred while trying to trigger Event:" + str(self) +
                                      ", on device:" + str(target_device) + "\n Output:" + str(output_text) +
                                      "\n Error:" + str(error_text))
        else:
            time.sleep(SystemEvent.SYSTEM_EVENT_SLEEP_TIME)
        return ret_code == 0

    def __str__(self):
        return self.get_name()

