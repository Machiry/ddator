__author__ = 'machiry'
import threading


class DDLogger:

    __stdout_lock = threading.Lock()

    def __init__(self, target_class_name, target_log_file=None, exit_on_failure=False):
        """

        :param target_class_name:
        :param target_log_file:
        :param exit_on_failure:
        :return:
        """
        self.target_class_name = target_class_name
        self.exit_on_failure = exit_on_failure
        self.log_fd = None
        if target_log_file is not None:
            self.log_fd = open(target_log_file, "w")
            self.local_lock = threading.Lock()

    @staticmethod
    def write_failure_message(text_to_write):
        with DDLogger.__stdout_lock:
            print('[@] ' + text_to_write)

    def _write(self, text_to_write):
        """

        :param text_to_write:
        :return:
        """
        if self.log_fd is None:
            with DDLogger.__stdout_lock:
                print(text_to_write)
        else:
            with self.local_lock:
                self.log_fd.write(text_to_write + "\n")

    def log_info(self, message):
        """

        :param message:
        :return:
        """
        self._write('[*] ' + self.target_class_name + ': ' + message)

    def log_success(self, message):
        """

        :param message:
        :return:
        """
        self._write('[+] ' + self.target_class_name + ': ' + message)

    def log_failure(self, message):
        """

        :param message:
        :return:
        """
        self._write('[-] ' + self.target_class_name + ': ' + message)
        if self.exit_on_failure:
            self._write('[#] ' + self.target_class_name + ': Exiting From Logger as Error Occured!')
            sys.exit(-1)

    def log_warning(self, message):
        """

        :param message:
        :return:
        """
        self._write('[!] ' + self.target_class_name + ': ' + message)
