from device_handler import DeviceHandler
from uiautomator import Device


class RealDeviceHandler(DeviceHandler):
    """

    """

    def __init__(self, target_device_id):
        assert target_device_id is not None, "Device ID cannot be None"
        self.target_device_id = target_device_id
        self.uiauto_object = Device(self.target_device_id)
        assert self.uiauto_object is not None, "UiAutomator cannot find the device with ID:" + \
                                               str(self.target_device_id)

    def reset_device(self):
        # TODO: implement this.
        raise NotImplementedError("Yet to implement.")

    def get_ui_handle(self):
        return self.uiauto_object

    def run_command(self, args):
        # TODO: implement this.
        raise NotImplementedError("Yet to implement.")

    def __hash__(self):
        return hash(self.target_device_id)

    def __eq__(self, other):
        if not isinstance(other, RealDeviceHandler):
            return False

        return self.target_device_id == other.target_device_id