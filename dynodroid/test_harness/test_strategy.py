__author__ = 'machiry'


class TestStrategy:

    def setup(self):
        raise NotImplementedError("setup not overridden.")

    def run_tests(self):
        raise NotImplementedError("run tests not overridden.")

    def cleanup(self):
        raise NotImplementedError("Clean up not overridden.")