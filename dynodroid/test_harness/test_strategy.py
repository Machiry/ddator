__author__ = 'machiry'

class TestStrategy:

    def setup(self, target_device, log_folder, target_app_handler):
        raise NotImplementedError("setup not overridden.")

    def get_name(self):
        return "TestStrategy"

    def run_tests(self):
        raise NotImplementedError("run tests not overridden.")

    def cleanup(self):
        raise NotImplementedError("Clean up not overridden.")

    def __str__(self):
        return self.get_name()
