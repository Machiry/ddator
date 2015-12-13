
class DeviceHandler:

    def reset_device(self):
        raise NotImplementedError("Reset Device not Implemented.")

    def run_command(self, args):
        raise NotImplementedError("Run Command not Implemented.")

    def get_ui_handle(self):
        raise NotImplementedError("Gets UIAutomator handle for the current device")
