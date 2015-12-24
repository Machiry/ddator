__author__ = 'machiry'
import threading
import datetime
import sys


class DDLogger(object):
    """
    Class that handles logging.
    """

    __stdout_lock = threading.Lock()

    def __init__(self, target_class_name, target_log_file=None, exit_on_failure=False):
        """
        Create a logger object.
        :param target_class_name: Class name to which the logger belongs.
        :param target_log_file: log file to be used for logging.
        :param exit_on_failure: flag which indicates the system to exit.
        :return: Target logger object.
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
        Write the provided text to the log.
        :param text_to_write: text to write to log.
        :return: None
        """
        with DDLogger.__stdout_lock:
                print(text_to_write)
        with self.local_lock:
            self.log_fd.write(text_to_write + "\n")
            self.log_fd.flush()

    def end_log(self):
        """
        End logging.
        :return: None
        """
        if self.log_fd is not None:
            with self.local_lock:
                self.log_fd.close()
                self.log_fd = None

    def log_info(self, message):
        """
        Log the provided message as info
        :param message: message to log
        :return: None
        """
        self._write('[*] ' + self.target_class_name + ' ' + str(datetime.datetime.now()) + ' ' + ': ' + message)

    def log_success(self, message):
        """
        Log the provided message as success.
        :param message: message to log.
        :return: None
        """
        self._write('[+] ' + self.target_class_name + ' ' + str(datetime.datetime.now()) + ' ' + ': ' + message)

    def log_failure(self, message):
        """
        Log the provided message as failure.
        :param message: message to log.
        :return: None
        """
        self._write('[-] ' + self.target_class_name + ' ' + str(datetime.datetime.now()) + ' ' + ': ' + message)
        if self.exit_on_failure:
            self._write('[#] ' + self.target_class_name + ' ' + str(datetime.datetime.now()) + ' ' +
                        ': Exiting From Logger as Error Occured!')
            sys.exit(-1)

    def log_warning(self, message):
        """
        Log the provided message as warning.
        :param message: message to log.
        :return: None
        """
        self._write('[!] ' + self.target_class_name + ' ' + str(datetime.datetime.now()) + ' ' + ': ' + message)
